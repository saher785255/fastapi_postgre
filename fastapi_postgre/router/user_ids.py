from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_postgre.client.database import get_db
from fastapi_postgre.controller import user_ids as ctrl
from  fastapi_postgre.models.tables import UserIDCreate, UserIDOut

router = APIRouter(prefix="/user_ids", tags=["user_ids"])

@router.post("/", response_model=UserIDOut)
def create_user_id(user_id_in: UserIDCreate, db: Session = Depends(get_db)):
    existing = ctrl.get_user_id(db, user_id_in.user_id)
    if existing:
        raise HTTPException(status_code=400, detail="user_id already exists")
    return ctrl.create_user_id(db, user_id_in.user_id)

@router.get("/", response_model=list[UserIDOut])
def list_user_ids(db: Session = Depends(get_db)):
    return ctrl.get_user_ids(db)