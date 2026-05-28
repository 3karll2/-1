from fastapi import APIRouter, Response, Depends, HTTPException
from src.database import SessionLocal
from src.models import User
from src.auth import get_password_hash, verify_password, create_access_token, get_current_user

router = APIRouter()

@router.post("/register")
def register(username: str, password: str):
    db = SessionLocal()
    hashed_pw = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    return {"message": "Користувач зареєстрований"}

@router.post("/login")
def login(response: Response, username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Невірні дані")
    
    token = create_access_token(data={"sub": username})
    response.set_cookie(key="access_token", value=token, httponly=True)
    return {"message": "Успішний вхід"}

@router.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {"user": current_user, "message": "Це захищена ручка!"}