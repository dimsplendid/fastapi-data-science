from fastapi import FastAPI, status, HTTPException
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

@app.patch("/posts/{id}", response_model=PostPublic)
async def partial_update(id: int, post_update: PostPartialUpate):
    try:
        post_db = db.posts[id]

        update_fields = post_update.dict(exclude_unset=True)

        updated_post = post_db.copy(update=update_fields)
        db.posts[id] = updated_post

        return updated_post
    
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)