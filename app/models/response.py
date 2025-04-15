import uuid
from sqlalchemy import UUID, Column, DateTime, func, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Response(Base):
    __tablename__ = "responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_id = Column(UUID(as_uuid=True), ForeignKey("forms.id"), nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    form = relationship("Form", back_populates="responses")