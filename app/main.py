from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import router
from app.db.session import engine, Base
from app.domain.models.users import User

@asynccontextmanager
async def lifespan(app=FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title='MindSpark',
    version='1.0.0',
    lifespan=lifespan
)

app.include_router(router)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0",
        port=8000,
        reload=True
        )