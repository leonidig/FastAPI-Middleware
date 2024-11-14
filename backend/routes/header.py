from typing import Optional
from fastapi import APIRouter, Header



main_router = APIRouter(prefix = "/main")



@main_router.get("/")
async def home(X_Custom_Header: Optional[str] = Header(None)):
    return {"header": X_Custom_Header}
