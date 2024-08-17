from datetime import datetime, date, time
from pydantic import BaseModel
from typing import Optional
import pytz

from src.enums import Status

class StudyPlanBase(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    start_time: time
    end_time: time

class StudyPlanCreate(StudyPlanBase):
    pass

class StudyPlanUpdate(StudyPlanBase):
    id: int
    status: Status

class StudyPlan(StudyPlanBase):
    id: int
    status: Status
    creation_time: Optional[datetime]
    last_modified: Optional[datetime]
    is_deleted: bool
    deletion_time: Optional[datetime]

    class Config:
        orm_mode = True