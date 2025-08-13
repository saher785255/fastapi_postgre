from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_postgre.client.database import get_db
from fastapi_postgre.controller import usernames as ctrl
from  fastapi_postgre.models.tables import UsernameCreate, UsernameOut

router = APIRouter(prefix="/usernames", tags=["usernames"])

@router.post("/", response_model=UsernameOut)
def create_username(username_in: UsernameCreate, db: Session = Depends(get_db)):
    existing = ctrl.get_username_by_name(db, username_in.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    return ctrl.create_username(db, username_in.username)

@router.get("/", response_model=list[UsernameOut])
def list_usernames(db: Session = Depends(get_db)):
    return ctrl.get_usernames(db)