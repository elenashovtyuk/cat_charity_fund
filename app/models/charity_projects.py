from sqlalchemy import Column, String, Text

# импортируем родительский класс для моделей
from .base import InvestBaseModel


class CharityProject(InvestBaseModel):
    """Модель проектов для пожертвований."""
    # поле name, имя проекта.
    # название проекта не более 100 символов
    # имя - уникальное
    # имя - не может быть пустым
    name = Column(String(100), unique=True, nullable=False)
    # поле description - описание,
    # обязательное текстовое поле
    # не менее одного символа
    description = Column(Text, nullable=False)
