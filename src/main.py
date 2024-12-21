"""FastAPI application"""

from fastapi import FastAPI
from pydantic import BaseModel

from lib.utils import add

app = FastAPI()


@app.get("/health_check")
def health_check():
    """Health check endpoint"""
    return "ok"


class AddRequest(BaseModel):
    """Add request model"""

    a: int
    b: int


@app.post("/add")
def add_endpoint(request: AddRequest):
    """Add endpoint"""
    return {"result": add(request.a, request.b)}
