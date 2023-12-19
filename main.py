import os
import pytesseract
from pdf2image import convert_from_path
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse


app = FastAPI()


def extract_text_from_pdf(file_path):
    # try:
    images = convert_from_path(file_path)
    images[0].save('output.png', 'PNG')
    text = ''
    for image in images:
        print(text)
        text += pytesseract.image_to_string(image)
    return text
    # except Exception as ex:
    #     raise HTTPException(status_code=500, detail=str(ex))


@app.get("/")
async def read_root():
    return {"Hello": "World"}
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as temp_file:
        temp_file.write(file.file.read())

    # Extract text from the PDF file
    path = os.path.join(os.getcwd(), file.filename)
    print(path)
    text_data = extract_text_from_pdf(path)
    print(text_data)
    os.remove(file.filename)

    return JSONResponse(content={'filename': file.filename, 'data': text_data}, status_code=200)
    # try:
    #     # Save the uploaded file to a temporary location
        
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
