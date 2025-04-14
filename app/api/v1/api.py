from fastapi import APIRouter

from app.api.v1.endpoints import auth, users #, forms, responses

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(forms.router, prefix="/forms", tags=["forms"])
# api_router.include_router(responses.router, prefix="/responses", tags=["responses"]) # Or nest under forms