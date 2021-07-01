from typing import Optional, List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from src import entities, crud
from src.database import engine, SessionLocal
from src.entities import UserEntity
from src.models import User, UserBase

app = FastAPI(
    title="py-template-api",
    servers=[{"url": "http://localhost:5000", "description": "DEV"}],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", tags=["users"], response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@app.get("/users/{user_id}", tags=["users"], response_model=User)
def find_user_by_id(user_id: str, db: Session = Depends(get_db)) -> User:
    user: UserEntity = crud.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User [{user_id}] not found")
    return user


@app.post("/users", tags=["users"], response_model=User)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


if __name__ == "__main__":
    entities.Base.metadata.create_all(bind=engine)
    uvicorn.run("src.app:app", host="localhost", port=5000, log_level="info")
