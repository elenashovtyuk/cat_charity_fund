from datetime import datetime
from sqlalchemy import Boolean, Column, String, Text, Integer, DateTime

# импортируем базовый класс для моделей
from app.core.db import Base


class CharityProject(Base):
    # поле name, имя проекта.
    # название проекта не более 100 символов
    # имя - уникальное
    # имя - не может быть пустым
    name = Column(String(100), unique=True, nullable=False)
    # поле description - описание,
    # обязательное текстовое поле
    # не менее одного символа
    description = Column(Text, nullable=False)
    # поле full_amount - требуемая сумма
    # целочисленное значение, больше 0
    full_amount = Column(Integer, nullable=False)
    # внесенная сумма, целочисленное поле,
    # значение по умолчанию 0
    invested_amount = Column(Integer, default=0)
    # поле fully_invested - булево значение
    # указывает на то, собрана ли нужная сумма для проекта
    # по умолчанию False
    fully_invested = Column(Boolean, default=False)
    # поле create_date - дата создания проекта,
    # можно добавлять автоматически в момент создания проекта
    create_date = Column(DateTime, default=datetime.utcnow())
    # поле close_date - дата закрытия проекта, DateTime,
    # проставляется автоматически в момент набора нужной суммы
    close_date = Column(DateTime)
