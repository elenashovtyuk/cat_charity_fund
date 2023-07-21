from sqlalchemy import Column, Text, Integer, ForeignKey
from .base import InvestBaseModel


class Donation(InvestBaseModel):
    """Модель для пожертвований."""
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
