# https://github.com/UB-Mannheim/tesseract/wiki
# https://github.com/tesseract-ocr/tessdata

import pytesseract
from PIL import ImageGrab
import os

img1 = ImageGrab.grabclipboard()

img1.save('pic_temp.png','PNG')

pytesseract.pytesseract.tesseract_cmd = r'F:\Tesseract-OCR\tesseract'

text1=pytesseract.image_to_string('pic_temp.png')

with open('text_temp.txt','w',encoding='gbk') as f:
    f.write(text1)

os.system('text_temp.txt')



