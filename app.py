import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import fitz
doc = fitz.open('css.pdf')
page = doc.load_page(1)
mat = fitz.Matrix(2,2)
pix = page.get_pixmap(matrix = mat)
output = 'css.png'
pix.save(output)

a = Image.open('css.png')
result = pytesseract.image_to_string(a, lang='kor')
print(result)


