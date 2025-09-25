from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
import io
from database import get_db
import pydantic_models

router = APIRouter(prefix="/uploads", tags=["uploads"])

@router.post("/delivery-logs", response_model=pydantic_models.FileUploadResponse)
async def upload_delivery_logs(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload and process delivery logs file (CSV or Excel)"""
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(400, "Only CSV and Excel files are supported")
    
    try:
        content = await file.read()
        
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(content))
        else:
            df = pd.read_excel(io.BytesIO(content))
        
        records_processed = len(df)
        
        return pydantic_models.FileUploadResponse(
            filename=file.filename,
            records_processed=records_processed,
            message=f"Successfully processed {records_processed} delivery records"
        )
        
    except Exception as e:
        raise HTTPException(500, f"Error processing file: {str(e)}")