from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from config.db import get_session

# ? Models
from models.categories import Categories
# ? Schemas
from schemas.categories import CategoriesInsertModel

router = APIRouter(
    tags=['categories'],
    responses={404: {'message': 'No encontrado'}})


@router.get('/' , status_code=status.HTTP_200_OK)
def show(session: Session = Depends(get_session)):  # params
    result = session.query(Categories).all()
    return result


@router.get('/{id}', status_code=status.HTTP_200_OK)
def find(id: int, session: Session = Depends(get_session)):
    result = session.query(Categories).get(id)
    if not result:
        raise HTTPException(status_code=400, detail=f'No row entry found with id {id}')
    return result


@router.post('/', status_code=status.HTTP_201_CREATED)
def insert(item: CategoriesInsertModel, session: Session = Depends(get_session)):
    # session.rollback() before add
    model = Categories(**item.dict())
    session.add(model)
    session.commit()
    return model


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, item: CategoriesInsertModel, session: Session = Depends(get_session)):
    result = session.query(Categories).filter_by(id=id).update(item.dict())
    if not result:
        raise HTTPException(status_code=400, detail=f'No row entry found with id: {id}')
    session.commit()
    return


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remove(id: int, session: Session = Depends(get_session)):
    result = session.query(Categories).filter_by(id = id).delete()
    if not result:
        raise HTTPException(status_code=400, detail=f'No row entry found with id: {id}')
    session.commit()
    return