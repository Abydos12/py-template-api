from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from app.database.entities import UserEntity
from app.database.repositories.users import UsersRepo
from app.models import User
from app.models.user import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=List[User])
def get_all_users(users: UsersRepo = Depends()):
    return users.get_all()


@router.post("", response_model=User)
def create_user(user: UserCreate, users: UsersRepo = Depends()):
    if users.get_by_username(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username [{user.username}] already exists",
        )
    return users.create(user)


@router.get("/{user_id}", response_model=User)
def find_user_by_id(
        user_id: str, users: UsersRepo = Depends()
) -> Union[RedirectResponse, UserEntity]:
    user: UserEntity = users.get_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User [{user_id}] not found"
        )
    return user


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: str, users: UsersRepo = Depends()):
    raise HTTPException(status.HTTP_418_IM_A_TEAPOT)


@router.patch("/{user_id}", status_code=status.HTTP_200_OK)
def partial_update_user(user_id: str, users: UsersRepo = Depends()):
    raise HTTPException(status.HTTP_418_IM_A_TEAPOT)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: str, users: UsersRepo = Depends()):
    raise HTTPException(status.HTTP_418_IM_A_TEAPOT)
