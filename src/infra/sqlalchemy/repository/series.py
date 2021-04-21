from sqlalchemy.orm import Session
from ..models import models
from ....schemas import schemas
from fastapi import HTTPException, status

from uuid import uuid4
randomId = str(uuid4())

def create(request: schemas.Series, db: Session):
    new_series = models.Series(     id = randomId,
                                    series_title = request.series_title,
                                    year_of_the_series = request.year_of_the_series,
                                    series_genre = request.series_genre,
                                    number_of_seasons = request.number_of_seasons)
    db.add(new_series)
    db.commit()
    db.refresh(new_series)
    return new_series

def show(db: Session):
    serires = db.query(models.Series).all()
    return serires

def show_title(series_title: str, db: Session):
    series = db.query(models.Series).filter(models.Series.series_title == series_title).first()
    if not series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"series with the title {series_title} not found")
    return series

def show_id(series_id: str, db: Session):
    series = db.query(models.Series).filter(models.Series.id == series_id).first()
    if not series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"series with the id {series_id} not found")
    return series

def remove_series(series_id: str, db: Session):
    series = db.query(models.Series).filter(models.Series.id == series_id)
    if not series.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"series with the id {series_id} not found")
    
    series.delete(synchronize_session=False)
    db.commit()
    return f'deleted'
