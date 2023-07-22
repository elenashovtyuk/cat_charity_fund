# app/crud/base.py
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


# базовый crud-класс, в котором будут реализованы все основные функции
# далее этот класс можно расширять
class CRUDBase:
    # при инициализации класса аттрибуту self.model будет присвоена
    # конкретная модель и далее все методы будут работать
    # именно с этой моделью
    def __init__(self, model):
        self.model = model

    async def get(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()

    async def get_multi(
            self,
            session: AsyncSession
    ):
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSession,
    ):
        # чтобы передатьполученные в запросе данные из Pydantic-схемы в ORM-модель
        # потребуется конвертровать схему в словарь
        # преобразуем схему в словарь можно с помощью метода dict()
        obj_in_data = obj_in.dict()
        # создаем объект модели(для этого распаковываем словарь с полученными даныыми)
        # т.е передаем пары ключ-значение для того, чтобы создать
        # экземпляр ORM-модели
        db_obj = self.model(**obj_in_data)
        # созданный объект добавляем в сессию
        session.add(db_obj)
        # записываем данные непосредственно в БД
        await session.commit()
        # обновляем объект db_obj
        await session.refresh(db_obj)
        # возвращаем только что созданный объект проекта пожертвований
        return db_obj

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self,
            db_obj,
            session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj
