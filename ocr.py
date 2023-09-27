import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

while True:
    cap = ImageGrab.grab(bbox=(515, 876, 998, 906))
    cap_arr = np.array(cap)
    res=cv2.resize(cap_arr,None,fx=1,fy=1,interpolation=cv2.INTER_CUBIC)
    cv2.imshow("", res)
    text = pytesseract.image_to_string(res)
    text = text.strip()
    if len(text) > 0:
        print(text)
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()