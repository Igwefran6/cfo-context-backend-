"""
Application entry point.

This file is responsible for:
- Creating the FastAPI app
- Registering API routes
- Nothing else

All business logic lives in app/context/builder.py
and API routes live in app/api.py
"""

from fastapi import FastAPI
from app.api.api import router  # This is your new api.py

# ---------------- FastAPI App ----------------

app = FastAPI(
    title="CFO Context API",
    description="Backend for the CFO pre-call context demo",
    version="0.1.0",
)

# Include all API endpoints under /api
app.include_router(router, prefix="/api")

# ---------------- Root Endpoint ----------------
@app.get("/")
def root():
    """
    Simple root endpoint for health/status check
    outside the /api prefix.
    """
    return {"message": "CFO Context Backend is running!"}