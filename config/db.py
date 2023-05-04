from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://postgres:root@127.0.0.1/webcomic_db'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

SessionLocal = sessionmaker(expire_on_commit=False, bind=engine, autoflush=False) #autocommit or expire ?


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
