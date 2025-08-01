from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_files.database import *
from api_files import models

models.Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(title="To_Do_API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
