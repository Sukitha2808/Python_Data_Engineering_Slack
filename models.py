# app/models.py
from sqlalchemy import Column, String, Date, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Shipment(Base):
    __tablename__ = "shipments"
    
    shipment_id = Column(String(20), primary_key=True, index=True)
    origin_warehouse = Column(String(20))
    destination_city = Column(String(100))
    ship_date = Column(Date)
    delivery_date = Column(Date)
    product_id = Column(String(20))
    quantity = Column(Integer)
    freight_cost = Column(Float)
    
    deliveries = relationship("DeliveryLog", back_populates="shipment")

class DeliveryLog(Base):
    __tablename__ = "delivery_logs"
    
    delivery_id = Column(String(50), primary_key=True, index=True)
    shipment_id = Column(String(50), ForeignKey("shipments.shipment_id"))
    carrier = Column(String(100))
    status = Column(String(50))
    delivery_duration_days = Column(Integer)
    damage_flag = Column(Boolean, default=False)  # Changed from TINYINT to Boolean
    proof_of_delivery_status = Column(String(50))
    
    shipment = relationship("Shipment", back_populates="deliveries")
    claims = relationship("Claim", back_populates="delivery")

class Claim(Base):
    __tablename__ = "claims"
    
    claim_id = Column(String(20), primary_key=True, index=True)
    delivery_id = Column(String(20), ForeignKey("delivery_logs.delivery_id"))
    reason = Column(String)
    amount_claimed = Column(Float)
    claim_status = Column(String(50), default="PENDING")
    claim_date = Column(Date)
    resolved_date = Column(Date, nullable=True)
    
    delivery = relationship("DeliveryLog", back_populates="claims")

class Vendor(Base):
    __tablename__ = "vendors"
    
    vendor_id = Column(String(20), primary_key=True, index=True)
    vendor_name = Column(String(100))
    product_id = Column(String(20))
    contract_start = Column(Date)
    contract_end = Column(Date)
    vendor_rating = Column(Float)
    country = Column(String(100))

class Inventory(Base):
    __tablename__ = "inventory"
    
    warehouse_id = Column(String(15), primary_key=True)
    product_id = Column(String(15), primary_key=True)
    stock_level = Column(Integer)
    reorder_threshold = Column(Integer)
    last_restock_date = Column(Date, nullable=True)
    next_restock_due = Column(Date, nullable=True)