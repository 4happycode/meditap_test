from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
import models
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


# Base Schemas
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase): # Inherit from UserBase
    def create(self, db: Session):
        # try exception
        try:
            db_user = models.User(**self.dict())
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered")


class UserUpdate(UserBase): # Inherit from UserBase
    pass


class User(UserBase): # Inherit from UserBase
    user_id: int

    class Config:
        orm_mode = True
