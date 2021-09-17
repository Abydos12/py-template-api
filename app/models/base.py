from pydantic import BaseModel, BaseConfig

from app import utils


class APIModel(BaseModel):
    class Config(BaseConfig):
        alias_generator = utils.snake2camel
        allow_population_by_field_name = True


class ORMModel(BaseModel):
    id: str

    class Config(BaseConfig):
        orm_mode = True
