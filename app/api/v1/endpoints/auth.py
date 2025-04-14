from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import user, token
from app.crud import crud_user
from app.core import security
from app.dependencies import get_db

router = APIRouter()

@router.post("/register", response_model=user.User, status_code=status.HTTP_201_CREATED)
async def register_user(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: user.UserCreate,
):
    """
    Create new user.
    """
    user = await crud_user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    user = await crud_user.create_user(db=db, user_in=user_in)
    return user


@router.post("/token", response_model=token.Token)
async def login_for_access_token(
    db: AsyncSession = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    OAuth2 compatible token login, get an access token for future requests.
    'username' field in the form is used for the email.
    """
    user = await crud_user.get_user_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
         raise HTTPException(status_code=400, detail="Inactive user")

    access_token = security.create_access_token(
        data={"sub": user.email} # 'sub' is standard claim for subject (user identifier)
    )
    return {"access_token": access_token, "token_type": "bearer"}