import uuid
from sqlalchemy import UUID, Column, DateTime, func, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Form(Base):
    __tablename__ = "forms"

    id = Column(UUID(as_uuid=True), primary_key=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    owner = relationship("User", back_populates="forms")
    responses = relationship("Response", back_populates="form", cascade="all, delete-orphan")