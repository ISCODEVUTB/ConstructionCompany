from pydantic import BaseModel, Field
from datetime import datetime

class PurchaseBase(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    supplier: str = Field(..., min_length=1)

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseOut(PurchaseBase):
    id: int
    purchase_date: datetime

    class Config:
        orm_mode = True