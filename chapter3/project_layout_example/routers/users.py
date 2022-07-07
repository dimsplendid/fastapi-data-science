from fastapi import APIRouter, HTTPException, status

from project_layout_example.models.user import User, UserCreate
from project_layout_example.db import db

router = APIRouter()

@router.get("/")
async def all() -> list[User]:
    return list(db.users.values())

@router.get("/{id}")
async def get(id: int) -> User:
    try:
        return db.users[id]
    except:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    new_id = max(db.users.keys() or (0,)) + 1
    user = User(id=new_id, **user_create.dict())
    db.users[new_id] = user
    return user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    try:
        db.users.pop(id)
    except:
        raise HTTPException(status.HTTP_404_NOT_FOUND)