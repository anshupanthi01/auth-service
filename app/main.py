from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.users.model import User
from app.auth.router import router as auth_router
from app.database.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Authentication & User Management API",
    version="1.0.0",
    description="Production-style authentication backend built with FastAPI.",
    lifespan=lifespan,
)

app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "message": "Authentication API is running."
    }