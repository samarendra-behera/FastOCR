import os
import pytesseract
from pdf2image import convert_from_path
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse


app = FastAPI()


def extract_text_from_pdf(file_path):
    images = convert_from_path(file_path)
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)
    return text


@app.get("/")
async def read_root():
    return {"Hello": "World"}
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as temp_file:
        temp_file.write(file.file.read())

    # Extract text from the PDF file
    path = os.path.join(os.getcwd(), file.filename)
    text_data = extract_text_from_pdf(path)
    name = file.filename
    os.remove(file.filename)

    return JSONResponse(content={'filename': name, 'data': text_data}, status_code=200)
    