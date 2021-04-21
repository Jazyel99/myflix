from sqlalchemy import Column, String, Integer, Date

from ..config.database import Base

class Series(Base):
    __tablename__ = "series"

    id = Column(String, primary_key=True)
    series_title = Column(String)
    year_of_the_series = Column(String)
    series_genre = Column(String)
    number_of_seasons = Column(Integer)