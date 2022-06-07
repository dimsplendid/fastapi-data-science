from fastapi import FastAPI

from project_layout_example.routers import users, posts

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(users.router, prefix="/users", tags=["users"])