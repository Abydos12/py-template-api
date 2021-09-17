from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.sql import Select

from app.database.entities import UserEntity
from app.database.repositories.base import DatabaseRepo
from app.models.user import UserCreate
from app.security.utils import hash_password


class UsersRepo(DatabaseRepo):
    def get_all(self) -> List[UserEntity]:
        stmt: Select = select(UserEntity)
        return self._session.execute(statement=stmt).scalars().all()

    def get_by_id(self, user_id: type(UserEntity.id)) -> Optional[UserEntity]:
        stmt = select(UserEntity).where(UserEntity.id == user_id)
        return self._session.execute(stmt).scalar_one_or_none()

    def get_by_username(
        self, username: type(UserEntity.username)
    ) -> Optional[UserEntity]:
        stmt = select(UserEntity).where(UserEntity.username == username)
        return self._session.execute(stmt).scalar_one_or_none()

    def create(self, user: UserCreate) -> UserEntity:
        db_user = UserEntity(
            username=user.username,
            hashed_password=hash_password(user.password),
            first_name=user.first_name,
            last_name=user.last_name,
            is_admin=user.is_admin,
        )
        self._session.add(db_user)
        self._session.flush()
        return db_user
