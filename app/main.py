import logging

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError

from app.core import settings
from app.database import engine, Base
from app.routes import router

app = FastAPI(
    title=settings.APP_NAME,
    servers=[{"url": "http://localhost:5000", "description": "DEV"}],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.exception_handler(SQLAlchemyError)
def handle_sql_alchemy_error(request, exc):
    logging.error(f"[DB] {exc} | Request: {request}")
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Fail to execute database operation",
    )


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host=settings.HOST, port=settings.PORT, log_level="info"
    )
