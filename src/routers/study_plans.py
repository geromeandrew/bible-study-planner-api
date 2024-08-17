from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict

from src.database import get_db
from src import models, schemas, services

router = APIRouter(
    prefix="/study_plans",
    tags=["study_plans"],
    responses={status.HTTP_404_NOT_FOUND: {"detail": "Study plan not found"}},
)

@router.get("/", response_model=List[schemas.StudyPlan])
def get_all_study_plans(db: Session = Depends(get_db)):
    return services.get_all_study_plans(db=db)

@router.get("/{id}", response_model=schemas.StudyPlan)
def get_study_plan_by_id(id: int, db: Session = Depends(get_db)):
    study_plan = services.get_study_plan_by_id(db=db, id=id)
    if not study_plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study plan not found")
    return study_plan

@router.post("/", response_model=Dict)
def create_study_plan(study_plan: schemas.StudyPlanCreate, db: Session = Depends(get_db)):
    return services.create_study_plan(db=db, study_plan=study_plan)

@router.put("/{id}", response_model=Dict)
def update_study_plan(id: int, study_plan: schemas.StudyPlanUpdate, db: Session = Depends(get_db)):
    db_study_plan = services.get_study_plan_by_id(db, id)
    if not db_study_plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study plan not found")
    return services.update_study_plan(db=db, study_plan=study_plan)

@router.delete("/{id}", response_model=Dict)
def delete_study_plan(id: int, db: Session = Depends(get_db)):
    db_study_plan = services.get_study_plan_by_id(db, id)
    if not db_study_plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study plan not found")
    return services.delete_study_plan(db=db, id=id)
