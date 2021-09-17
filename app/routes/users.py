from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from app.database.entities import UserEntity
from app.database.repositories.users import UsersRepo
from app.models import User
from app.models.user import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[User])
def get_all_users(users: UsersRepo = Depends(UsersRepo)):
    return users.get_all()


@router.get("/{user_id}", response_model=User)
def find_user_by_id(
    user_id: str, users: UsersRepo = Depends(UsersRepo)
) -> Union[RedirectResponse, UserEntity]:
    user: UserEntity = users.get_by_id(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User [{user_id}] not found")
    return user


@router.post("/", response_model=User)
def create_user(user: UserCreate, users: UsersRepo = Depends(UsersRepo)):
    return users.create(user=user)
