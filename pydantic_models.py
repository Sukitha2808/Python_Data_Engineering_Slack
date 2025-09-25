from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import date

# Base Schemas
class ShipmentBase(BaseModel):
    origin_warehouse: str
    destination_city: str
    ship_date: date
    delivery_date: date
    product_id: str
    quantity: int
    freight_cost: float

class DeliveryLogBase(BaseModel):
    shipment_id: str
    carrier: str
    status: str
    delivery_duration_days: int
    damage_flag: bool = False
    proof_of_delivery_status: str

class ClaimBase(BaseModel):
    delivery_id: str
    reason: str
    amount_claimed: float
    claim_status: str = "PENDING"
    claim_date: date = Field(default_factory=date.today)

class VendorBase(BaseModel):
    vendor_name: str
    product_id: str
    contract_start: date
    contract_end: date
    vendor_rating: float
    country: str

class InventoryBase(BaseModel):
    warehouse_id: str
    product_id: str
    stock_level: int
    reorder_threshold: int
    last_restock_date: Optional[date] = None
    next_restock_due: Optional[date] = None

# Response Schemas
class ShipmentCreate(ShipmentBase):
    pass

class ShipmentResponse(ShipmentBase):
    shipment_id: str
    model_config = ConfigDict(from_attributes=True)

class DeliveryLogResponse(DeliveryLogBase):
    delivery_id: str
    model_config = ConfigDict(from_attributes=True)

class ClaimResponse(ClaimBase):
    claim_id: str
    resolved_date: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)

class VendorResponse(VendorBase):
    vendor_id: str
    model_config = ConfigDict(from_attributes=True)

class InventoryResponse(InventoryBase):
    model_config = ConfigDict(from_attributes=True)

# Analytics Schemas
class InventoryHealth(BaseModel):
    warehouse_id: str
    product_id: str
    stock_level: int
    reorder_threshold: int
    stock_status: str
    days_until_restock: Optional[int] = None

class ClaimsSummary(BaseModel):
    carrier: str
    total_claims: int
    total_shipments: int
    claim_percentage: float
    avg_claim_amount: float

class FileUploadResponse(BaseModel):
    filename: str
    records_processed: int
    message: str