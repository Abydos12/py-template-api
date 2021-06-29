import re

from pydantic import BaseModel, BaseConfig


class APIModel(BaseModel):
    class Config(BaseConfig):
        alias_generator = lambda s: re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)
        allow_population_by_field_name = True


class ORModel(BaseModel):
    id: str

    class Config(BaseConfig):
        orm_mode = True


class UserBase(APIModel):
    first_name: str
    last_name: str


class User(UserBase, ORModel):
    pass
