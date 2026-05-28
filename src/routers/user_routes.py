from fastapi import APIRouter, Depends
from src.auth import get_current_user

router = APIRouter()

@router.get("/my-profile")
def my_profile(current_user: str = Depends(get_current_user)):
    return {"message": f"Привіт, {current_user}, це доступно тільки авторизованим!"}