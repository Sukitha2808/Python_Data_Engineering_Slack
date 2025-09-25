from sqlalchemy.orm import Session
from sqlalchemy import func
import models

def get_carrier_performance(db: Session):
    """Get carrier performance metrics (optional)"""
    result = db.query(
        models.DeliveryLog.carrier,
        func.count(models.DeliveryLog.delivery_id).label('total_deliveries'),
        func.avg(models.DeliveryLog.delivery_duration_days).label('avg_delivery_time'),
        func.sum(models.DeliveryLog.damage_flag.cast(models.Integer)).label('damaged_shipments'),
        func.count(models.Claim.claim_id).label('total_claims')
    ).outerjoin(
        models.Claim, models.DeliveryLog.delivery_id == models.Claim.delivery_id
    ).group_by(
        models.DeliveryLog.carrier
    ).all()
    
    return [
        {
            'carrier': carrier,
            'total_deliveries': total_deliveries,
            'avg_delivery_time': round(avg_delivery_time or 0, 2),
            'damaged_shipments': damaged_shipments,
            'total_claims': total_claims
        }
        for carrier, total_deliveries, avg_delivery_time, damaged_shipments, total_claims in result
    ]