from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from routers import claims, inventory, shipments, uploads

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Supply Chain API",
    description="API for managing supply chain operations and analytics",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include only the required routers
app.include_router(claims.router)
app.include_router(inventory.router)
app.include_router(shipments.router)
app.include_router(uploads.router)

@app.get("/")
async def root():
    return {
        "message": "Supply Chain API",
        "version": "1.0.0",
        "endpoints": {
            "claims_summary": "/claims/summary",
            "inventory_health": "/inventory/health", 
            "log_shipment": "/shipments/",
            "upload_delivery_logs": "/uploads/delivery-logs"
        },
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "supply-chain-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)