from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud
import pydantic_models

router = APIRouter(prefix="/shipments", tags=["shipments"])

@router.post("/", response_model=pydantic_models.ShipmentResponse)
async def log_shipment(shipment: pydantic_models.ShipmentCreate, db: Session = Depends(get_db)):
    """Add a new shipment record"""
    return crud.create_shipment(db, shipment)