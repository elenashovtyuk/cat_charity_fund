# from app.models.base import InvestBaseModel
# from app.core.db import get_async_session
# from fastapi import Depends
# from sqlalchemy.ext.asyncio import  AsyncSession
# from datetime import datetime
# from app.models.base import InvestBaseModel
# from typing import List, Optional


# # создаем корутину, которая будет отвечать за процесс инвестирования
# # далее эту корутину будем вызывать при создании нового проекта или пожертвования
# # то есть, в API-функциях эндпоинтов для создания новых проектов или пожертвований
# async def investing(
#     session: AsyncSession,
#     base_model: InvestBaseModel
# ) -> List[Optional(InvestBaseModel)]:
#     pass












# def close_donation_of_project(*objs: InvestBaseModel, session: AsyncSession) -> None:
#     for obj in objects:
#         # проверяем, что внесенная сумма меньше, чем требуемая сумма сбора
#         if obj.invested_amount < obj.full_amount:
#             continue
#         # если же внесенная сумма стала равна требуемой сумме сбора
#         # то булево значение fully_invested становится True -
#         # то есть, нужная сумма набрана
#         obj.fully_invested = True
#         # после чего устанавливается дата закрытия проекта
#         obj.close_date = datetime.now()
#         session.add(obj)
