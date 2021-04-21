from fastapi import FastAPI
from src.infra.sqlalchemy.config.database import Base, engine
from src.routes import series
from src.infra.sqlalchemy.models import models

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(series.router)