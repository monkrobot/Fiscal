from datetime import datetime
from sqlalchemy import (Boolean, Column, ForeignKey, Integer,
                        DateTime)
from sqlalchemy.orm import relationship

from fiscal.db import Base


class Cashbox(Base):
    __tablename__ = "cashboxes"

    id = Column(Integer, primary_key=True, index=True)
    inn = Column(Integer, index=True)
    kpp = Column(Integer)
    registration_num = Column(Integer)


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, index=True)
    inn  = Column(Integer, index=True)
    kpp = Column(Integer)
    price = Column(Integer)
    cashbox_id = Column(Integer, ForeignKey("cashboxes.id"))
    
    #cashbox = relationship("Cashbox", back_populates="trips")
