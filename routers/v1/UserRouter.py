from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.UserSchema import UserSchema

UserRoute = APIRouter(
    prefix="/v1/users",
    tags=["user"],
)

@UserRoute.get("/", response_model=List[UserSchema])
def index():
    # Simulate fetching users from a database
    return [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

@UserRoute.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int):
    # Simulate fetching a user from a database by their ID
    return {"id": user_id, "name": f"User {user_id}"}

@UserRoute.post("/", response_model=UserSchema)
def create_user(user: UserSchema):
    # Simulate creating a user in a database
    return user

@UserRoute.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema):
    # Simulate updating a user in a database by their ID
    return user

@UserRoute.delete("/{user_id}")
def delete_user(user_id: int):
    # Simulate deleting a user from a database by their ID
    return {"detail": "User deleted"}