from pydantic import BaseModel, Field, validator
from typing import Optional

class CategoriesInsertModel(BaseModel):
    name: str = Field(max_length=50)
    description: Optional[str] = Field(max_length=250)

class CategoriesUpdatetModel(BaseModel):
    name: Optional[str] = Field(max_length=50)
    description: Optional[str] = Field(max_length=250)

    # @validator('name')
    # def size_is_some(cls, v):
    #     if v == 'Hola mundo':
    #        raise ValueError('sum of numbers greater than 42')
    #     return v
