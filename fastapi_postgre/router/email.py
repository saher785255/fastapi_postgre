from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_postgre.client.database import get_db
from fastapi_postgre.models.tables import EmailCreate, EmailOut
from fastapi_postgre.controller.email import create_email, get_emails

router = APIRouter()

@router.post("/email", response_model=EmailOut)
def add_email(email: EmailCreate, db: Session = Depends(get_db)):
    return create_email(db, email.email)

@router.get("/emails", response_model=list[EmailOut])
def list_emails(db: Session = Depends(get_db)):
    return get_emails(db)
