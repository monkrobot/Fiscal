from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fiscal.crud import crud
from fiscal.schemas import schema
from fiscal.dependencies import get_db

router = APIRouter(
    prefix="/data"
)

@router.get("/")
async def root():
    return {"Info": "This is data service"}


@router.post("/cashbox", response_model=schema.Cashbox)
async def post_cashbox(data: schema.Cashbox, db: Session = Depends(get_db)):
    cashbox = await crud.get_cashbox(db, data)
    if cashbox:
        HTTPException(status_code=400, detail="Cashbox is already registered")
    cashbox = await crud.post_cashbox(db, data)
    return cashbox


@router.get("/cashbox", response_model=schema.Cashbox)
async def get_cashbox(data: schema.Cashbox, db: Session = Depends(get_db)):
    cashbox = await crud.get_cashbox(db, data)
    return cashbox


@router.post("/trip", response_model=schema.Trip)
async def post_trip(data: schema.Trip, db: Session = Depends(get_db)):
    b = await crud.post_trip(db, data)
    return b
