import uuid

from sqlalchemy import Column, String, Boolean

from ...database import Base


def default(context):
    print(context)
    return context.get_current_parameters()["hashed_password"]


class UserEntity(Base):
    __tablename__ = "users"

    id: str = Column(
        String, primary_key=True, index=True, default=lambda: str(uuid.uuid4())
    )
    username: str = Column(String(64), unique=True, nullable=False)
    hashed_password: str = Column(String(512), nullable=False, default=default)
    is_admin: bool = Column(Boolean, nullable=False, default=False)

    first_name: str = Column(String(64))
    last_name: str = Column(String(64))

    def __repr__(self):
        return f"UserEntity(username='{self.username}')"
