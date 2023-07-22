from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.core.db import get_async_session
# from app.models.charity_projects import CharityProject
from app.schemas.charity_projects import CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
from app.crud.charity_projects import charity_project_crud
from app.api.validators import check_charity_project_exists, check_name_duplicate
from typing import List

router = APIRouter()


# опишем эндпоинт для операции POST
@router.post(
    '/charity_project/',
    response_model=CharityProjectDB)
# API-функция, обработчик запроса
# эта функция будет использовать асинхронную crud-функцию
# поэтому она и сама должна быть асинхронной
async def create_new_charity_project(
    # укажем схему
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """Обработка запроса на создание нового проекта пожертвований."""
    new_charity_project = await charity_project_crud.create(charity_project, session)
    return new_charity_project


# опишем эндпоинт для операции GET
@router.get(
    '/сharity_project/',
    response_model=List[CharityProjectDB],
)
async def get_all_charity_projecs(
    session: AsyncSession = Depends(get_async_session)
):
    all_charity_projects = await charity_project_crud.get_multi(session)
    return all_charity_projects


# опишем эндпоинт для операции PATCH
@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB
)
async def partially_update_charity_project(
    charity_project_id: int,
    # JSON-данные, переданные пользователем
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    # перед тем, как внести изменения в конкретный проект
    # нужно убедиться - существует ли указанный проект в БД
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    # если в переданных пользователем данных есть название проекта, то проверяем
    # что это название уникально
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    # далее, если проверки прошли, вызываем crud-функцию update
    # т.е вносим изменения в указанный проект пожертвований
    # в параметрах указываем проект, который нужно изменить
    # данные из update-запроса пользователя
    charity_project = await charity_project_crud.update(
        charity_project, obj_in, session
    )
    # возвращаем измененный проект пожертвований
    return charity_project


# опишем эндпоинт для операции DELETE
@router.delete(
    '/{charity_project_id}',
    response_model=CharityProjectDB
)
async def remove_charity_project(
    charity_project_id: int,
    session: AsyncSession = Depends(get_async_session),
):

    # Выносим повторяющийся код в отдельную корутину.
    # проверяем с помощью корутины-валидатора, что указанный
    # проект существует
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    charity_project = await charity_project_crud.remove(
        charity_project, session
    )
    return charity_project
