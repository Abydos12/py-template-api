from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import make_session


class DatabaseRepo:
    _session: Session

    def __init__(self, session: Session = Depends(make_session)):
        self._session = session
