from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool

from fiscal.settings import SQLALCHEMY_DATABASE_URL


sync_engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
#Sync_session = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
#engine = create_async_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
#SessionLocal = sessionmaker(
#    engine, expire_on_commit=False, class_=AsyncSession
#)

Base = declarative_base()
