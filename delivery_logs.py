from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import crud
import pydantic_models

router = APIRouter(prefix="/delivery-logs", tags=["delivery_logs"])

@router.get("/", response_model=List[pydantic_models.DeliveryLogResponse])
async def read_delivery_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all delivery logs"""
    delivery_logs = crud.get_delivery_logs(db, skip=skip, limit=limit)
    return delivery_logs

@router.get("/{delivery_id}", response_model=pydantic_models.DeliveryLogResponse)
async def read_delivery_log(delivery_id: int, db: Session = Depends(get_db)):
    """Get a specific delivery log by ID"""
    delivery_log = crud.get_delivery_log(db, delivery_id)
    if delivery_log is None:
        raise HTTPException(status_code=404, detail="Delivery log not found")
    return delivery_log

@router.post("/", response_model=pydantic_models.DeliveryLogResponse)
async def create_delivery_log(delivery_log: pydantic_models.DeliveryLogBase, db: Session = Depends(get_db)):
    """Create a new delivery log"""
    return crud.create_delivery_log(db, delivery_log)