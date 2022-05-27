from datetime import datetime
from pydantic import BaseModel


class Cashbox(BaseModel):
    inn: int
    kpp: int
    registration_num: int

    class Config:
        orm_mode = True


class Trip(BaseModel):
    datetime: datetime
    inn: int
    kpp: int
    price: int

    class Config:
        orm_mode = True


class Resonse(BaseModel):
    msg: str
