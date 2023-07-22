from fastapi import FastAPI

# импортируем настройки проекта из config.py
from app.core.config import settings
from app.api.routers import main_router

# создание объекта приложения
# устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения укажем аттрибут app_title объекта settings
app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

# подключаем главный роутер
app.include_router(main_router)
