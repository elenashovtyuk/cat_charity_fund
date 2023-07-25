from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
# импортируем объект donation_crud, который включает в себя все методы базового
# CRUD-класса
from app.crud.donation import donation_crud
# имопртируем модель
# from app.models.donation import Donation
from app.models import User
from app.schemas.donation import DonationCreate, DonationRead
from app.core.user import current_superuser, current_user
from typing import List
# from app.services.investing import investing

# создаем объект роутера
router = APIRouter()


# опишем 1-ый эндпоинт для получения списка всех пожертвований
# просматривать все пожертвования может только суперюзер
@router.get(
    '/',
    # укажем схему ответа на запрос - должен вернуться список пожертвований
    response_model=List[DonationRead],
    response_model_exclude_none=True,
    # запросить список всех пожертвований может только суперюзер
    dependencies=[Depends(current_superuser)],
)
# API-функция
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров."""
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    # укажем схему ответа
    response_model=List[DonationRead],
    # исключим пустые поля из ответа
    response_model_exclude_none=True,
    # текущий пользователь может запросить инфо о своих пожертвованиях
    dependencies=[Depends(current_user)],
    # укажем аттрибуты, которые нужно исключить из ответа
    response_model_exclude={
        'user_id',
        'invest_amount',
        'fully_invested',
        'close_date'
    }
)
# API-функция, обработчик запроса
async def get_all_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    # CRUD-функция
    return await donation_crud.get_user_donations(session, user)


# опишем эндпоинт для операции POST
@router.post(
    '/',
    # укажем схему ответа
    response_model=DonationRead,
    response_model_exclude_none=True,
    # укажем в параметрах декоратора пути в сете аттрибуты,
    # которые нужно исключить из ответа
    response_model_exclude={
        'user_id',
        'invested_amount',
        'fully_invested',
        'close_date'
    },
    # сделать пожертвование может любой зарегистрированный пользователь
    dependencies=[Depends(current_user)],
)
# API-функция, обработчик POST-запроса
async def create_donation(
    # на вход функции подаем JSON-данные отправленные пользователем
    donation: DonationCreate,
    # указываем зависимость - т.е текущего юзера
    # так как сделать пожертвование может любой зарегистрированный пользователь
    user: User = Depends(current_user),
    # указываем зависимость - сессию
    session: AsyncSession = Depends(get_async_session)
):
    # СRUD-функция
    # вызываем объект donation_crud с методом
    # для создания нового объекта пожертвования
    new_donation = await donation_crud.create(
        # передаем JSON-данные из запроса, пользователя и сессию
        donation,
        session,
        user
    )
#     # при создании нового пожертвования должен запускаться процесс инвестирования
#     # увеличение внесенной суммы пожертвований(invested_amount),
#     #  установка значений fully_invested (собрана или нет нужная сумма)
#     # и даты закрытия сбора (close_date) - (при необходимости)
#     session.add_all(await investing(session, new_donation))
#     await session.commit()
#     await session.refresh(new_donation)
    # возвращается новый объект пожертвования
    return new_donation
