import asyncio

from sqlalchemy.future import select
from sqlalchemy.orm import Session

from fiscal.schemas import schema
from fiscal import models


async def post_cashbox(db: Session, data: schema.Cashbox):
    new_cashbox = models.Cashbox(
        inn=data.inn,
        kpp=data.kpp,
        registration_num=data.registration_num
    )
    db.add(new_cashbox)
    db.commit()
    db.refresh(new_cashbox)
    return new_cashbox


async def get_cashbox(db: Session, data: schema.Cashbox):
    query = (models.Cashbox.inn == data.inn and
             models.Cashbox.kpp == data.kpp and
             models.Cashbox.registration_num == data.registration_num)
    cashbox = db.execute(
                select(models.Cashbox).where(query))
    cashbox = cashbox.scalars().first()
    return cashbox


async def post_trip(db: Session, data: schema.Trip):
    query = (models.Cashbox.inn == data.inn and
             models.Cashbox.kpp == data.kpp)
    cashbox_id = db.execute(
                select(models.Cashbox.id).where(query))
    cashbox_id = cashbox_id.scalars().first()
    if not cashbox_id:
        return {"msg": f"There is no such cashbox inn: {data.inn}, " \
                       f"kpp: {data.kpp}"}
    new_trip = models.Trip(
        datetime=data.datetime,
        inn=data.inn,
        kpp=data.kpp,
        price=data.price,
        cashbox_id=cashbox_id
    )
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip
