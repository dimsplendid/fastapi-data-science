from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
async def upload_multiple_file(files: list[UploadFile] = File(...)):
    return [{
        "file_name": file.filename,
        "content_type": file.content_type
    } for file in files]