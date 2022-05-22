from pydantic import BaseModel

class UserProfile(BaseModel):
    nickname: str
    location: str | None = None
    subscribed_newsletter: bool = True

user = UserProfile(nickname="jdoe")
print(user)