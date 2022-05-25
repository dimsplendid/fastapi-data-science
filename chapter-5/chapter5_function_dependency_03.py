from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostPartialUpate(BaseModel):
    title: str | None = None
    content: str | None = None

class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

class PostDB(PostBase):
    id: int
    nb_views: int = 0

class DummyDatabase:
    posts: dict[int, PostDB] = {}

db = DummyDatabase()

async def get_post_or_404(id: int) -> PostDB:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

app = FastAPI()

@app.post(
    "/posts", 
    status_code=status.HTTP_201_CREATED,
    response_model=PostPublic
)
async def create(post_create: PostCreate):
    new_id = max(db.posts.keys() or (0,)) + 1
    post = PostDB(id=new_id, **post_create.dict())
    db.posts[new_id] = post
    return post

@app.get("/posts/{id}", response_model=PostPublic)
async def get(post: PostDB = Depends(get_post_or_404)):
    return post

@app.patch("/posts/{id}", response_model=PostPublic)
async def update(
    post_update: PostPartialUpate, 
    post: PostDB = Depends(get_post_or_404)
):
    updated_post = post.copy(update=post_update.dict())
    db.posts[post.id] = updated_post
    return updated_post
    
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: PostDB = Depends(get_post_or_404)):
    db.posts.pop(post.id)