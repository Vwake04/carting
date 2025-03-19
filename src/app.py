from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.endpoints.items import router as items_router
from src.api.endpoints.users import router as users_router
from src.core.config import settings
from src.db.init_db import init_db

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the database on startup
@app.on_event("startup")
async def startup_db_client():
    init_db()


# Include routers
app.include_router(items_router, prefix="/api/items", tags=["items"])
app.include_router(users_router, prefix="/api/users", tags=["users"])


@app.get("/")
def read_root():
    return {
        "app_name": settings.APP_NAME,
        "version": "0.1.0",
        "message": "Welcome to the Carting API",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
