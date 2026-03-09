from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")
router.include_router("", prefix="/")

from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="Star Wars API",
        version="1.0.0",
    )

    app.include_router(router)

    return app