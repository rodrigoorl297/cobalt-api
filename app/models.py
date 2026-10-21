from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student: Mapped[str] = mapped_column(String(120), index=True)
    course: Mapped[str] = mapped_column(String(120))
    progress: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(40), default="active")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
