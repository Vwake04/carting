import uvicorn

from src.core.config import settings
from src.app import app

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG
    )
