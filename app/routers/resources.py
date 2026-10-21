from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.db import get_db
from app.models import Enrollment
from app.schemas import EnrollmentIn, EnrollmentOut

router = APIRouter(prefix="/enrollments", tags=["enrollments"])


@router.get("", response_model=list[EnrollmentOut])
def list_items(db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return db.query(Enrollment).order_by(Enrollment.id.desc()).all()


@router.post("", response_model=EnrollmentOut, status_code=status.HTTP_201_CREATED)
def create_item(body: EnrollmentIn, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = Enrollment(**body.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/{item_id}", response_model=EnrollmentOut)
def get_item(item_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = db.get(Enrollment, item_id)
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return row
