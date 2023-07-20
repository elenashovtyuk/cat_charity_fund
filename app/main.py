from fastapi import FastAPI

# импортируем настройки проекта из config.py
from app.core.config import settings

# создание объекта приложения
# устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения укажем аттрибут app_title объекта settings
app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)
