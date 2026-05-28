from fastapi import FastAPI
from src.routers.users import router as users_router

app = FastAPI(title="User CRUD API")

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI CRUD Lab 3"}