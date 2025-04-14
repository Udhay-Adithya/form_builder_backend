from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.dependencies import get_current_user # Use get_current_user directly
# from app.dependencies import get_current_active_user

router = APIRouter()

@router.get("/me", response_model=schemas.User)
async def read_users_me(
    current_user: models.User = Depends(get_current_user),
):
    """
    Get current user.
    """
    return current_user

# Add other user endpoints later if needed (e.g., update user)