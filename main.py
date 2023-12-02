from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections

app = FastAPI(
    title="Fast API COURSE MANAGEMENT",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Pabitra",
        "email": "pabitrapandit2001@gmail.com",
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)