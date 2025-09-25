from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import List
import models
import pydantic_models
from datetime import date

# Shipment operations
def create_shipment(db: Session, shipment: pydantic_models.ShipmentCreate):
    db_shipment = models.Shipment(**shipment.dict())
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

# Analytics operations
def get_claims_summary(db: Session):
    """Return claim percentages per carrier"""
    result = db.query(
        models.DeliveryLog.carrier,
        func.count(models.Claim.claim_id).label('total_claims'),
        func.count(models.DeliveryLog.delivery_id).label('total_shipments'),
        func.avg(models.Claim.amount_claimed).label('avg_claim_amount')
    ).outerjoin(
        models.Claim, models.DeliveryLog.delivery_id == models.Claim.delivery_id
    ).group_by(
        models.DeliveryLog.carrier
    ).all()
    
    summary = []
    for carrier, total_claims, total_shipments, avg_claim_amount in result:
        claim_percentage = (total_claims / total_shipments * 100) if total_shipments > 0 else 0
        summary.append(pydantic_models.ClaimsSummary(
            carrier=carrier,
            total_claims=total_claims,
            total_shipments=total_shipments,
            claim_percentage=round(claim_percentage, 2),
            avg_claim_amount=round(avg_claim_amount or 0, 2)
        ))
    
    return summary

def get_inventory_health(db: Session):
    """Return stock and reorder status"""
    inventory_items = db.query(models.Inventory).all()
    
    health_data = []
    for item in inventory_items:
        if item.stock_level <= item.reorder_threshold:
            stock_status = "CRITICAL"
        elif item.stock_level <= item.reorder_threshold * 1.5:
            stock_status = "LOW"
        else:
            stock_status = "HEALTHY"
        
        days_until_restock = None
        if item.next_restock_due:
            days_until_restock = (item.next_restock_due - date.today()).days
        
        health_data.append(pydantic_models.InventoryHealth(
            warehouse_id=item.warehouse_id,
            product_id=item.product_id,
            stock_level=item.stock_level,
            reorder_threshold=item.reorder_threshold,
            stock_status=stock_status,
            days_until_restock=days_until_restock
        ))
    
    return health_data