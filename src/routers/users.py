from fastapi import APIRouter, HTTPException, status
from src.schemas.users import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

db_users = {}
id_counter = 1

@router.get("/", response_model=list[UserResponse])
def get_users():
    return list(db_users.values())

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    return db_users[user_id]

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    global id_counter

    for u in db_users.values():
        if u["email"] == user_data.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = {
        "id": id_counter,
        "username": user_data.username,
        "email": user_data.email,
        "age": user_data.age
    }
    db_users[id_counter] = new_user
    id_counter += 1
    return new_user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    
    current_user = db_users[user_id]
    
    update_dict = user_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        current_user[key] = value
        
    db_users[user_id] = current_user
    return current_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    del db_users[user_id]
    return None