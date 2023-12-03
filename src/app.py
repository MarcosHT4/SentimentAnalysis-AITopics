from fastapi import FastAPI
from src.config import get_settings
from src.routers import (
    status,
    prediction,
    reports,
    analysis,
    gptanalysis
)
from fastapi.middleware.cors import CORSMiddleware



SETTINGS = get_settings()
app = FastAPI(title=SETTINGS.api_name, version=SETTINGS.revision)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status.router)
app.include_router(prediction.router)
app.include_router(reports.router)
app.include_router(analysis.router)
app.include_router(gptanalysis.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)