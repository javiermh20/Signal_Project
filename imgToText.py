from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\javie\AppData\Local\Tesseract-OCR\tesseract.exe'

img = Image.open('p1.jpg')
text = tess.image_to_string(img) 
text1 = text.upper()
text2 = text1.strip()
text3 = 'hipopotomonstrosesquipedialofobia'

for i in range(len(text2)):
    caracter = text2[i]
    print("En el índice {} tenemos a '{}'".format(i, caracter))
    url = 'senas\{}.jpg'.format(caracter)
    im = Image.open(url)
    im.show()
