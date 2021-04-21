from pydantic import BaseModel

class Series(BaseModel):
    series_title: str
    year_of_the_series: str
    series_genre: str
    number_of_seasons: int

class ShowSeries(Series):
    id: str
    class Config():
        orm_mode = True