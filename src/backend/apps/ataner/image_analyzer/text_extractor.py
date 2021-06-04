from PIL import Image
import pytesseract as tess


class TextExtractor:
    def __init__(self, user_ocr_path=r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
        """
        C: Users <username> AppData Local Tesseract-OCR tesseract.exe
        """
        # WINDOWS path to OCR
        tess.pytesseract.tesseract_cmd = user_ocr_path

    def extract_from_file(self, imagepath="text.png"):
        try:
            img = Image.open(imagepath)
            text = tess.image_to_string(img)
            return text
        except tess.pytesseract.TesseractNotFoundError:
            return "[OCR] No ewidentie coś nie pykło :<"

