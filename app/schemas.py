from datetime import datetime

from pydantic import BaseModel, Field


class EnrollmentIn(BaseModel):
    student: str = Field(min_length=1, max_length=120)
    course: str
    progress: str
    status: str = "active"


class EnrollmentOut(EnrollmentIn):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
