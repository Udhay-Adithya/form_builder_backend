import uuid
from typing import List, Optional, Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload


from app.models.form import Form
from app.schemas.form import FormCreate, FormUpdate, FormData

async def create_form(db: AsyncSession, *, form_in: FormCreate, owner_id: uuid.UUID) -> Form:
    """
    Create a new form.
    """
    # Pydantic V2+ .model_dump() replaces .dict()
    form_data_dict = form_in.data.model_dump()
    db_form = Form(
        data=form_data_dict,
        owner_id=owner_id
    )
    db.add(db_form)
    await db.commit()
    await db.refresh(db_form, attribute_names=['id', 'created_at']) # Refresh essential fields
    # Eager load owner for the response object
    await db.refresh(db_form, attribute_names=['owner'])
    return db_form


async def get_form(db: AsyncSession, *, form_id: uuid.UUID) -> Optional[Form]:
    """
    Get a single form by ID, including owner details.
    """
    result = await db.execute(
        select(Form)
        .options(selectinload(Form.owner)) # Eager load owner
        .filter(Form.id == form_id)
    )
    return result.scalars().first()


async def get_forms_by_owner(
    db: AsyncSession, *, owner_id: uuid.UUID, skip: int = 0, limit: int = 100
) -> List[Form]:
    """
    Get all forms owned by a specific user, with pagination.
    Includes owner details.
    """
    result = await db.execute(
        select(Form)
        .options(selectinload(Form.owner)) # Eager load owner
        .filter(Form.owner_id == owner_id)
        .offset(skip)
        .limit(limit)
        .order_by(Form.created_at.desc()) # Optional: order by creation date
    )
    return result.scalars().all()


async def update_form(
    db: AsyncSession, *, db_form: Form, form_in: FormUpdate
) -> Form:
    """
    Update an existing form.
    """
    # Pydantic V2+ .model_dump() replaces .dict()
    # Use exclude_unset=True to only update fields that were actually passed
    update_data = form_in.model_dump(exclude_unset=True)

    if "data" in update_data and update_data["data"] is not None:
        # If 'data' is being updated, replace the whole JSON structure
        # You could implement more granular updates (merging JSON) if needed
        db_form.data = update_data["data"] # Assuming form_in.data is the structured FormData

    # Update other top-level fields of the Form model if they existed
    # for field, value in update_data.items():
    #    if field != "data": # Exclude 'data' as it's handled above
    #        setattr(db_form, field, value)

    db.add(db_form)
    await db.commit()
    await db.refresh(db_form)
    # Ensure owner is loaded if needed after refresh
    await db.refresh(db_form, attribute_names=['owner'])
    return db_form


async def remove_form(db: AsyncSession, *, form_id: uuid.UUID) -> Optional[Form]:
    """
    Delete a form by ID.
    Also deletes associated responses due to cascade="all, delete-orphan".
    """
    result = await db.execute(select(Form).filter(Form.id == form_id))
    db_form = result.scalars().first()
    if db_form:
        await db.delete(db_form)
        await db.commit()
    return db_form # Return the deleted object (or None if not found)