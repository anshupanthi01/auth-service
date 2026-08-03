from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppError


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(AppError)
    async def app_exception_handler(request: Request, exc: AppError):
        return JSONResponse(
            status_code= exc.status_code,
            content={
                "success": False,
                "error": {
                    "message": exc.description,
                    "status_code": exc.status_code 
                },
            }
        )
