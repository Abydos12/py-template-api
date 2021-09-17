from pydantic import validator
from pydantic.fields import ModelField

from .base import APIModel, ORMModel


class UserBase(APIModel):
    username: str
    first_name: str
    last_name: str
    is_admin: bool = False


class UserCreate(UserBase):
    password: str

    @validator("username", "first_name", "last_name", "password")
    def password_validation(cls, v, field: ModelField):
        if len(v) < 2:
            raise ValueError(f"{field.alias} too short, must be 2 characters or more")


class User(UserBase, ORMModel):
    pass
