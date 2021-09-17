from pathlib import Path

__all__ = ["ROOT_PATH", "LOCAL_DB_URI"]

ROOT_PATH = Path(".")
LOCAL_DB_URI = f"sqlite:///{ROOT_PATH / '..' / 'app.db'}"
