from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import crud
import pydantic_models

router = APIRouter(prefix="/vendors", tags=["vendors"])

@router.get("/", response_model=List[pydantic_models.VendorResponse])
async def read_vendors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all vendors"""
    vendors = crud.get_vendors(db, skip=skip, limit=limit)
    return vendors

@router.get("/{vendor_id}", response_model=pydantic_models.VendorResponse)
async def read_vendor(vendor_id: int, db: Session = Depends(get_db)):
    """Get a specific vendor by ID"""
    vendor = crud.get_vendor(db, vendor_id)
    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

@router.post("/", response_model=pydantic_models.VendorResponse)
async def create_vendor(vendor: pydantic_models.VendorCreate, db: Session = Depends(get_db)):
    """Create a new vendor"""
    return crud.create_vendor(db, vendor)

@router.get("/performance/", response_model=List[pydantic_models.VendorPerformance])
async def get_vendor_performance(db: Session = Depends(get_db)):
    """Get vendor performance metrics"""
    return crud.get_vendor_performance(db)