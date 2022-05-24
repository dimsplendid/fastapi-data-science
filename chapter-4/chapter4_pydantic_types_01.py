from pydantic import (
    BaseModel, 
    EmailStr, 
    HttpUrl,
    ValidationError
)

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

# Invalid email
try:
    User(
        email="jdoe",
        website="https://www.example.com"
    )
except ValidationError as e:
    print(e)

# Valid
user = User(
    email="jdoe@example.com",
    website="https://www.example.com",
)

print(user)