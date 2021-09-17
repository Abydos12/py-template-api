import re

from app.database import Session


def snake2camel(s: str):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
