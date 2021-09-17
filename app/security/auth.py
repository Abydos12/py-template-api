from datetime import datetime, timedelta


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.core import settings
from app.database.repositories import UsersRepo
from app.security.utils import verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def authenticate_user(username: str, password: str, users: UsersRepo = Depends()):
    user = users.get_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
        # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username")
        # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    return user


def verify_token(token: str = Depends(oauth2_scheme)):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No token found in headers Authorization",
        )
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Token error:{e}"
        )


def get_auth_user(claims: dict = Depends(verify_token), users: UsersRepo = Depends()):
    username: str = claims.get("usr")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Token malformed"
        )
    user = users.get_by_username(username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User not recognized"
        )
    return user
