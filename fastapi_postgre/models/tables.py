from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from fastapi_postgre.client.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session

# SQLAlchemy models
class UsernameTable(Base):
    __tablename__ = "usernames"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)  # auto timestamp

class UserIDTable(Base):
    __tablename__ = "user_ids"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)  # auto timestamp


# Pydantic schemas
class UsernameBase(BaseModel):
    username: str

class UsernameCreate(UsernameBase):
    pass

class UsernameOut(UsernameBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class UserIDBase(BaseModel):
    user_id: int

class UserIDCreate(UserIDBase):
    pass

class UserIDOut(UserIDBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True


# Insert
def create_username(db: Session, username_str: str, created_at: datetime = None) -> UsernameTable:
    obj = UsernameTable(
        username=username_str,
        created_at=created_at or datetime.utcnow()
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
