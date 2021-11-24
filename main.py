import imghdr
import os
import shutil
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
i = 1
str_list = []
key = input("Enter keyword")
for filename in os.scandir(r'G:\images\whatsapp'):
    if filename.is_file():
        string = pytesseract.image_to_string(filename.path)
        str_list.append(string.lower() if str else ' ')
        print(f"image number {i}")
        i += 1
i = 0
while key != "0":
    for filename in os.scandir(r'G:\images\whatsapp'):
        if key in str_list[i] and imghdr.what(filename) == 'jpeg':
            try:
                shutil.copy(filename.path, r"G:\images\whatsapp\sorted")
            except Exception as e:
                print(filename.name, '\n')
        print(i)
        i += 1
    key = input("Enter key . 0 for end")
    i = 0
