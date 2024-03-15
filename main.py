from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Models with engine
models.Base.metadata.create_all(bind=engine)

# Declare app
app = FastAPI()

# Dependency database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD API Operations

# Create new user
@app.post("/api/users/", response_model=schemas.User) # decorator with pydantic response model
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): # include params schemas & session db
    return user.create(db)

# Retrieve list of all users data
@app.get("/api/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# Retrieve single user data by user_id
@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    # If user not found in db
    if user is None:
        # Return http exception
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update existing user data by user_id
@app.put("/api/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    # check exist user data
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    for attr, value in user.dict().items():
        setattr(db_user, attr, value)
    db.commit()
    db.refresh(db_user)
    
    return db_user

# Delete user data by user_id
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    
    return {"message": "User deleted successfully"}
