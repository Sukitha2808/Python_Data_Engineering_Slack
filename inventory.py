from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import crud
import pydantic_models

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/health", response_model=List[pydantic_models.InventoryHealth])
async def get_inventory_health(db: Session = Depends(get_db)):
    """Return stock and reorder status"""
    return crud.get_inventory_health(db)