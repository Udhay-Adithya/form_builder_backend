import uuid
from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from datetime import datetime

# Properties to receive via API on creation
# The 'data' is a flexible dictionary mapping field IDs to answers
class ResponseCreate(BaseModel):
    data: Dict[str, Any] = Field(..., example={
        "fld_abc123": "Alice Smith",
        "fld_def456": "alice@example.com",
        "fld_ghi789": "blue",
        "fld_jkl012": ["react", "python"]
    })

# Properties shared by models stored in DB
class ResponseInDBBase(BaseModel):
    id: uuid.UUID
    form_id: uuid.UUID
    data: Dict[str, Any]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True # Pydantic V2+


# Properties to return to client
class Response(ResponseInDBBase):
    pass # Keep it simple for now, could add 'form' relation if needed


# Properties stored in DB
class ResponseInDB(ResponseInDBBase):
    pass