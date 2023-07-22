from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.core.db import get_async_session
from app.models.charity_projects import CharityProject
from app.schemas.charity_projects import CharityProjectCreate
from app.crud.charity_projects import charity_project_crud
router = APIRouter()


# опишем эндпоинт для операции Create
@router.post(
    '/charity_project/',
    response_model=CharityProject)
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
