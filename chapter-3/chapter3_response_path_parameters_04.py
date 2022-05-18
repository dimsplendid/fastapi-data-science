from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

class PublicPost(BaseModel):
    title: str

# Dummy database
posts = {
    1: Post(title="Hello", nb_views=100),
}

app = FastAPI()

@app.get("/posts/{id}", response_model=PublicPost)
async def get_post(id: int):
    return posts[id]

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    posts.pop(id, None)
    return None

