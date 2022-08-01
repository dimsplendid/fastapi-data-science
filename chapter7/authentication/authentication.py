from tortoise.exceptions import DoesNotExist

from authentication.models import (
    AccessToken,
    AccessTokenTortoise,
    UserDB,
    UserTortoise,
)
from authentication.password import verify_password


async def authenticate(email: str, password: str) -> UserDB | None:
    try:
        user = await UserTortoise.get(email=email)
    except DoesNotExist:
        return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    return UserDB.from_orm(user)

async def create_access_token(user: UserDB) -> AccessToken:
    access_token = AccessToken(user_id=user.id)
    access_token_tortoise = await AccessTokenTortoise.create(
        **access_token.dict()
    )
    
    return AccessToken.from_orm(access_token_tortoise)