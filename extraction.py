import PyPDF2
import docx
import pdf2image
import pytesseract
from io import BytesIO

def extract_text(file: BytesIO, file_type: str) -> str:
    """Extract text from the uploaded file based on its type."""
    if file_type == 'txt':
        return file.read().decode('utf-8')
    elif file_type == 'docx':
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file_type == 'pdf':
        #try:
            pdf = PyPDF2.PdfReader(file)
            text = ''
            for page in range(len(pdf.pages)):
                text += pdf.pages[page].extract_text()     
            if len(text.strip()) < 100:  # Threshold for image-based PDFs
                return ocr_pdf(file)
            return text
        #except Exception as e:
            #return ocr_pdf(file)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

def ocr_pdf(file: BytesIO) -> str:
    """Perform OCR on image-based PDFs."""
    images = pdf2image.convert_from_bytes(file.read())
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)
    return text