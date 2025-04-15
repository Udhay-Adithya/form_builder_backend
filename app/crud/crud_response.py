import uuid
from typing import List, Optional, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.response import Response
from app.schemas.response import ResponseCreate

async def create_response(
    db: AsyncSession, *, response_in: ResponseCreate, form_id: uuid.UUID
) -> Response:
    """
    Create a new response for a specific form.
    """
    # Pydantic V2+ .model_dump() replaces .dict()
    db_response = Response(
        data=response_in.model_dump()["data"], # Get the inner data dict
        form_id=form_id,
        # submitter_id can be added here if tracking logged-in submitters
    )
    db.add(db_response)
    await db.commit()
    await db.refresh(db_response)
    return db_response


async def get_response(db: AsyncSession, *, response_id: uuid.UUID) -> Optional[Response]:
    """
    Get a single response by ID.
    """
    result = await db.execute(
        select(Response).filter(Response.id == response_id)
    )
    return result.scalars().first()


async def get_responses_by_form(
    db: AsyncSession, *, form_id: uuid.UUID, skip: int = 0, limit: int = 1000 # Higher limit common for responses
) -> List[Response]:
    """
    Get all responses for a specific form, with pagination.
    """
    result = await db.execute(
        select(Response)
        .filter(Response.form_id == form_id)
        .offset(skip)
        .limit(limit)
        .order_by(Response.created_at.asc()) # Often oldest first for responses
    )
    return result.scalars().all()

# Update/Delete for responses are less common for end-users,
# but could be added for admins/owners later.