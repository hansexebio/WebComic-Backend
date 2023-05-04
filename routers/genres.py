from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from config.db import get_session


from pydantic import BaseModel, Field, validator
from typing import Optional
# ? Models
from models.genres import Genres

# ? Schemas

class Item(BaseModel):
    name: Optional[str] = Field(max_length=50)
    description: Optional[str] = Field(max_length=250)

    # @validator('name')
    # def size_is_some(cls, v):
    #     if v == 'Hola mundo':
    #        raise ValueError('sum of numbers greater than 42')
    #     return v


router = APIRouter(
    tags=['genres'],
    responses={404: {'message': 'No encontrado'}})


@router.get('/' , status_code=status.HTTP_200_OK)
def show(session: Session = Depends(get_session)):  # params
    result = session.query(Genres).all()
    return result


@router.get('/{id}', status_code=status.HTTP_200_OK)
def find(id: int, session: Session = Depends(get_session)):
    result = session.query(Genres).get(id)
    if not result:
        raise HTTPException(status_code=400, detail=f'No row entry found with id {id}')
    return result


@router.post('/', status_code=status.HTTP_201_CREATED)
def insert(item: Item, session: Session = Depends(get_session)):
    # session.rollback() before add
    model = Genres(**item.dict())
    session.add(model)
    session.commit()
    return model


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, item: Item, session: Session = Depends(get_session)):
    result = session.query(Genres).filter_by(id=id).update(item.dict())
    if not result:
        raise HTTPException(status_code=400, detail=f'No row entry found with id: {id}')
    session.commit()
    return


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove(id: int, session: Session = Depends(get_session)):
    result = session.query(Genres).filter_by(id = id).delete()
    if not result:
        raise HTTPException(status_code=400, detail=f'No row entry found with id: {id}')
    session.commit()
    return