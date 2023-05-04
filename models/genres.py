from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from datetime import datetime
from config.db import Base, engine


class Genres(Base):
    __tablename__  = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)

Base.metadata.create_all(engine)