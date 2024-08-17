from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import study_plans
from src.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Bible Study Planner API',
    description='API for managing Bible study plans',
    version='1.0.0'
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(study_plans.router)