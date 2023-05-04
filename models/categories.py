from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from datetime import datetime
from config.db import Base, engine


class Categories(Base):
    __tablename__  = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(250))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)

Base.metadata.create_all(engine)