from fastapi import APIRouter

# Import endpoint modules
from app.api.v1.endpoints import auth, users, forms, responses # Add forms, responses

api_router = APIRouter()

# Include routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(forms.router, prefix="/forms", tags=["Forms"])
# Include the responses router - note it handles paths like /forms/{form_id}/responses/
api_router.include_router(responses.router, tags=["Responses"]) # No prefix needed here as paths are absolute