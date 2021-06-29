import uuid
from typing import List, Union

from sqlalchemy.orm import Session

from src.entities import UserEntity
from src.models import User, UserBase


def get_users(db: Session) -> List[UserEntity]:
    return db.query(UserEntity).all()


def get_user_by_id(
    db: Session, user_id: type(UserEntity.id)
) -> Union[UserEntity, None]:
    return db.query(UserEntity).filter(UserEntity.id == user_id).first()


def create_user(db: Session, user: UserBase) -> UserEntity:
    db_user = UserEntity(**user.dict(), id=str(uuid.uuid4()))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
