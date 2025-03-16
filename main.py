from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(title="User Management API")

# Pydantic model for User
class User(BaseModel):
    id: int
    name: str
    phone_no: str
    address: str

# Pydantic model for UserUpdate (without id field since it's in the path)
class UserUpdate(BaseModel):
    name: str
    phone_no: str
    address: str

# In-memory storage for users
users_db = {}

# Create a new user
@app.post("/users/", status_code=201)
async def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db[user.id] = user
    return {"message": "User created successfully"}

# Search users by name - IMPORTANT: This route must be defined BEFORE the /users/{user_id} route
@app.get("/users/search", response_model=List[User])
async def search_users(name: str = Query(..., description="Name to search for")):
    found_users = [user for user in users_db.values() if name.lower() in user.name.lower()]
    return found_users

# Read user by id - This route should come AFTER the /users/search route
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# Update user details
@app.put("/users/{user_id}")
async def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user while preserving the ID
    current_user = users_db[user_id]
    updated_user = User(
        id=user_id,
        name=user_update.name,
        phone_no=user_update.phone_no,
        address=user_update.address
    )
    users_db[user_id] = updated_user
    return {"message": "User updated successfully"}

# Delete user by id
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}

# Root endpoint for API documentation information
@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API. Access the documentation at /docs"}