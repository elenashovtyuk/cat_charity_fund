from sqlalchemy import Column, String, Text

from .base import InvestBaseModel


class CharityProject(InvestBaseModel):
    """Модель проектов для пожертвований."""
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
