from fastapi import FastAPI, status
from fastapi.responses import FileResponse

from os import path

app = FastAPI()

@app.get("/cat")
async def get_cat():
    root_directory = path.dirname(__file__)
    picture_path = path.join(root_directory, 'cat.jpg')
    return FileResponse(picture_path)