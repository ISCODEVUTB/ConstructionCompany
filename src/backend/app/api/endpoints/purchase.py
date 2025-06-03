from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.backend.app.api.database.schemas.purchase_db import PurchaseCreate, PurchaseOut
from src.backend.app.api.models.purchase import Purchase
from src.backend.app.api.database import get_db

router = APIRouter(prefix="/purchases", tags=["purchases"])

@router.post("/", response_model=PurchaseOut, status_code=201)
def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase