import os
from fastapi import Request, HTTPException, status
from dotenv import load_dotenv
load_dotenv()

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

async def verify_internal_api_key(request: Request, call_next):
    api_key = request.headers.get("x-internal-api-key")
    if not api_key or api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key")
    response = await call_next(request)
    return response
