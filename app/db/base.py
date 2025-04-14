# app/db/base.py
# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.user import User  # noqa F401 - Import user model
# Import other models here as you create them
# from app.models.form import Form # noqa F401
# from app.models.response import Response # noqa F401