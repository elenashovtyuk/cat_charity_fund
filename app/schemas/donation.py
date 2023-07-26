from datetime import datetime
from pydantic import BaseModel, Extra, PositiveInt, Field
from typing import Optional
from app.constants import DEFAULT_INVESTING_AMOUNT


class DonationBase(BaseModel):
    """Базовая схема."""
    full_amount: PositiveInt = Field(..., title='Сумма пожертвования')
    comment: Optional[str] = Field(None, title='Комментарий к пожертвованию')

    class Config:
        title = 'Базовая схема пожертвования'


class DonationCreate(DonationBase):
    """Схема для создания пожертвования."""
    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'full_amount': 1000,
                'comment': 'QRKot'
            }
        }


class DonationDB(DonationBase):
    """Схема пожертвования для получения из базы обычным пользователем."""
    id: int = Field(..., title='ID пожертвования')
    create_date: datetime = Field(..., title='Дата внесения пожертвования')

    class Config:
        title = 'Схема пожертвования для получения'
        orm_mode = True
        schema_extra = {
            'example': {
                'comment': 'QRKot',
                'full_amount': 500,
                'id': 2,
                'create_date': '2023-07-21T23:54:05.177Z'
            }
        }


class DonationDBSuper(DonationDB):
    """Схема пожертвования для получения из базы суперпользователем."""
    user_id: Optional[int] = Field(None, title='ID пользователя')
    invested_amount: int = Field(
        DEFAULT_INVESTING_AMOUNT,
        title='Сколько вложено',
    )
    fully_invested: bool = Field(False, title='Вложена полная сумма')
    close_date: Optional[datetime] = Field(None, title='Дата вложения')

    class Config:
        title = 'Схема пожертвования для получения (advanced)'
        orm_mode = True
        schema_extra = {
            'example': {
                'comment': 'QRKot',
                'full_amount': 500,
                'id': 2,
                'create_date': '2023-07-21T23:54:05.177Z',
                'user_id': 1,
                'invested_amount': 200,
                'fully_invested': 0
            }
        }


# # схема для получения пожертвований пользователя, сделавшего запрос
# class DonationRead(DonationBase):
#     """
#     Схема для получения всех пожертвований пользователя, сделавшего запрос.
#     """
#     id: int
#     user_id: int
#     invested_amount: int
#     fully_invested: bool
#     create_date: datetime
#     close_time: Optional[datetime]

#     # добавляем подкласс Config с аттрибутом schema_extra
#     class Config:
#         orm_mode = True
#         schema_extra = {
#             'example': {
#                 'full_amount': 1000,
#                 'comment': 'QRKot',
#                 'id': 1,
#                 'create_date': "2019-08-24T14:15:22Z"
#             }
#         }


# # # схема для получения списка всех пожертвований
# # # наследуем от схемы DonationRead, так как она включает в себя
# # # аттрибуты базовой схемы, а также два дполонительных аттрибута
# # # которые также должны быть и у текущей схемы
# # # соблюдение принципа DRY
# # class DonationReadAll(DonationRead):
# #     """Схема для получения всех пожертвований."""
# #     user_id: int
# #     invested_amount: NonNegativeInt
# #     fully_invested: bool
# #     close_date: datetime

# #     # добавляем подкласс Config c аттрибутом schema_extra
# #     # который позволяет добавить пример запроса
# #     class Config:
# #         schema_extra = {
# #             'example': {
# #                 'full_amount': 1000,
# #                 'comment': 'QRKot',
# #                 'id': 1,
# #                 'create_date': "2019-08-24T14:15:22Z",
# #                 'user_id': 1,
# #                 'invested_amount': 10000,
# #                 'fully_invested': True,
# #                 'close_date': "2019-08-24T14:15:22Z"
# #             }
# #         }
