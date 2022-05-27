from datetime import datetime
import sqlalchemy
from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class PostDB(PostBase):
    id: int


metadata = sqlalchemy.MetaData()

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True, autoincrement=True),
    sqlalchemy.Column("publication_date",
                      sqlalchemy.DateTime(), nullalble=False),
    sqlalchemy.Column("title", sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column("content", sqlalchemy.text(), nullable=False)
)
