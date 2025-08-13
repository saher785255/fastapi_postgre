from sqlalchemy.orm import Session
from fastapi_postgre.models.tables import UsernameTable
from datetime import datetime

def create_username(db: Session, username_str: str, created_at: datetime = None) -> UsernameTable:
    obj = UsernameTable(
        username=username_str,
        created_at=created_at or datetime.utcnow()
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_usernames(db: Session):
    return db.query(UsernameTable).all()

def get_username_by_name(db: Session, username_str: str):
    return db.query(UsernameTable).filter(UsernameTable.username == username_str).first()
