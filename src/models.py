from sqlalchemy import Column, Integer, String, Date, Time, Enum, DateTime, Boolean
from datetime import datetime
import pytz

from src.enums import Status
from src.database import Base

class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    status = Column(Enum(Status), nullable=False, default=Status.NEW)

    creation_time = Column(DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Manila')))
    last_modified = Column(DateTime)
    is_deleted = Column(Boolean, nullable=False, default=False)
    deletion_time = Column(DateTime)