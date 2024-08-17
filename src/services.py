from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
import pytz

from . import models, schemas

def get_all_study_plans(db: Session) -> list[schemas.StudyPlan]:
    """Retrieve all study plans."""
    return db.query(models.StudyPlan).all()

def get_study_plan_by_id(db: Session, id: int) -> Optional[schemas.StudyPlan]:
    """Retrieve a study plan by ID."""
    return db.query(models.StudyPlan).filter(models.StudyPlan.id == id).first()

def create_study_plan(db: Session, study_plan: schemas.StudyPlanCreate) -> dict:
    """Create a new study plan."""
    try:
        db_study_plan = models.StudyPlan(**study_plan.dict())
        db.add(db_study_plan)
        db.commit()
        db.refresh(db_study_plan)
        return {"status_code": 201, "detail": "Study plan created successfully"}
    except Exception as e:
        db.rollback()
        raise e

def update_study_plan(db: Session, study_plan: schemas.StudyPlanUpdate) -> dict:
    """Update an existing study plan."""
    db_study_plan = db.query(models.StudyPlan).filter(models.StudyPlan.id == study_plan.id).first()

    if not db_study_plan:
        raise Exception("Study plan not found")
    try:
        db_study_plan.id = study_plan.id
        db_study_plan.status = study_plan.status
        db_study_plan.last_modified = datetime.now(pytz.timezone('Asia/Manila'))
        db_study_plan.name = study_plan.name
        db_study_plan.description = study_plan.description
        db_study_plan.start_date = study_plan.start_date
        db_study_plan.end_date = study_plan.end_date
        db_study_plan.start_time = study_plan.start_time
        db_study_plan.end_time = study_plan.end_time
        db.commit()
        db.refresh(db_study_plan)
        return {"status_code": 200, "detail": "Study plan updated successfully"}
    except Exception as e:
        db.rollback()
        raise e

def delete_study_plan(db: Session, id: int) -> dict:
    """Soft delete a study plan."""
    db_study_plan = get_study_plan_by_id(db, id)
    try:
        db_study_plan.is_deleted = True
        db_study_plan.deletion_time = datetime.now(pytz.timezone('Asia/Manila'))
        db.commit()
        db.refresh(db_study_plan)
        return {"status_code": 200, "detail": "Study plan deleted successfully"}
    except Exception as e:
        db.rollback()
        raise e