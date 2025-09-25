from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import crud
import pydantic_models

router = APIRouter(prefix="/claims", tags=["claims"])

@router.get("/summary", response_model=List[pydantic_models.ClaimsSummary])
async def get_claims_summary(db: Session = Depends(get_db)):
    """Return claim percentages per carrier"""
    return crud.get_claims_summary(db)