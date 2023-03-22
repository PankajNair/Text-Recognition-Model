import cv2
import pytesseract
import numpy as np

def noise_remove(image):
    kernel = np.ones((1,1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1,1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
img = cv2.imread('1.jpg')
img  = cv2.resize(img, None, fx = 0.85, fy = 0.85)
blurImg = noise_remove(img)
blurImg = cv2.fastNlMeansDenoising(blurImg, None, 7, 21, 21)
sharpImg = cv2.addWeighted(img, 0.15, blurImg, 0.85, 0)

text = pytesseract.image_to_string(sharpImg)
print(text)

boxes = pytesseract.image_to_data(sharpImg)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(sharpImg, (x,y), (w+x,h+y), (0,0,255), 1)
            cv2.putText(sharpImg, b[11], (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (50,50,255), 1)

cv2.imshow('Result',sharpImg)
cv2.waitKey(0)