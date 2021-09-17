from .base import APIModel, ORMModel


class UserBase(APIModel):
    username: str
    is_admin: bool
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase, ORMModel):
    pass
