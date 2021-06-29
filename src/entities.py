from sqlalchemy import Column, String

from src.database import Base


class UserEntity(Base):
    __tablename__ = "users"

    id: str = Column(String, primary_key=True, index=True)
    first_name: str = Column(String)
    last_name: str = Column(String)
