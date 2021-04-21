from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from ..infra.sqlalchemy.config import database
from ..schemas import schemas
from ..infra.sqlalchemy.repository import series

get_db = database.get_db

router = APIRouter(
    tags=['series'],
    prefix="/series"
)

@router.get('/', status_code=200, response_model=List[schemas.ShowSeries])
def show_all_series(db: Session = Depends(get_db)):
    return series.show(db)

@router.get('/showTitle{series_title}', status_code=200, response_model=schemas.ShowSeries)
def show_series_title(series_title: str, db: Session = Depends(get_db)):
    return series.show_title(series_title, db)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowSeries)
def create_new_series(request: schemas.Series, db: Session = Depends(get_db)):
    return series.create(request, db)

@router.delete('/{series_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_series(series_id: str, db: Session = Depends(get_db)):
    return series.remove_series(series_id, db)

@router.get('/showID/{show_series_id}', status_code=200, response_model=schemas.ShowSeries)
def show_series_id(show_series_id: str, db: Session = Depends(get_db)):
    return series.show_id(show_series_id, db)