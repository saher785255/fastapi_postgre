from sqlalchemy.orm import Session
from fastapi_postgre.models.tables import UserIDTable
from datetime import datetime

def create_user_id(db: Session, user_id_value: int, created_at: datetime = None) -> UserIDTable:
    obj = UserIDTable(
        user_id=user_id_value,
        created_at=created_at or datetime.utcnow()  # use provided or current UTC time
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_user_ids(db: Session):
    return db.query(UserIDTable).all()

def get_user_id(db: Session, user_id_value: int):
    return db.query(UserIDTable).filter(UserIDTable.user_id == user_id_value).first()
