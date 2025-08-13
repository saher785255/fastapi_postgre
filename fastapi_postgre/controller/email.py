from sqlalchemy.orm import Session
from datetime import datetime
from fastapi_postgre.models.tables import EmailTable

def create_email(db: Session, email_str: str, created_at: datetime = None) -> EmailTable:
    obj = EmailTable(
        email=email_str,
        created_at=created_at or datetime.utcnow()
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_emails(db: Session):
    return db.query(EmailTable).all()

def get_email_by_address(db: Session, email_str: str):
    return db.query(EmailTable).filter(EmailTable.email == email_str).first()
