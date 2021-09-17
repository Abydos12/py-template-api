import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import LOCAL_DB_URI

engine = create_engine(
    LOCAL_DB_URI, connect_args={"check_same_thread": False}, echo=True
)
Session = sessionmaker(bind=engine)

Base = declarative_base()


def make_session():
    with Session.begin() as session:
        try:
            yield session
        except Exception as e:
            logging.error(f"[DB] {e}")
