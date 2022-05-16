from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class UserFormat(str, Enum):
    SHORT = 'short'
    FULL = 'full'

@app.get('/users')
async def get_user(format: UserFormat):
    return {'format': format}