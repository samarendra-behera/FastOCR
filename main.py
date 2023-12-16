import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF

app = FastAPI()


def extract_text_from_pdf(file_path):
    text_data = {}
    
    try:
        doc = fitz.open(file_path)
        
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text_data[f'page{page_num + 1}'] = {'text': page.get_text()}
        
        doc.close()
    except Exception as e:
        # Handle exceptions such as invalid PDF format, password-protected PDF, etc.
        raise e
    
    return text_data


@app.get("/")
async def read_root():
    return {"Hello": "World"}
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file to a temporary location
        with open(file.filename, "wb") as temp_file:
            temp_file.write(file.file.read())

        # Extract text from the PDF file
        text_data = extract_text_from_pdf(file.filename)
        os.remove(file.filename)

        return JSONResponse(content={'filename': file.filename, 'data': text_data}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
