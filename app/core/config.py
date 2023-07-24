from pydantic import BaseSettings
from typing import Optional
from pydantic import BaseSettings, EmailStr
# для работы с переменными окружения создаем класс,
# унаследованный от BaseSettings из библиотеки pydantic
# этот класс позволяет считывать из оперюсистемы переменные окружения
# напрямую обращаться к файлу .env


class Settings(BaseSettings):
    # добавим аттрибут app_title - в нем будет храниться название приложения
    # в аннотации укажем, что это строковый тип данных и зададим значение
    # по умолчанию
    app_title: str = 'QRKot'
    app_description: str = 'Сервис для поддержки котиков!'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    # подкласс Config содержит спец.аттрибут env_file
    # в этом аттрибуте укажем имя файла с переменными окружения
    class Config:
        env_file = '.env'


# создаем глобальную переменную settings с экземпляром класса Settings
# чтобы его можно было импортировать в любую часть приложения, где
# потребуется доступ к настройкам
settings = Settings()
