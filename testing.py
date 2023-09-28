import time
import random
from typing import Deque
import pyautogui
from AppOpener import open
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
pair=[("owo lb",1),
    ("owo pray",1),
    ("owo wc",1)]
def Check(x1,y1,x2,y2):
    while True:
        cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        cap_arr = np.array(cap)
        res=cv2.resize(cap_arr,None,fx=1,fy=1,interpolation=cv2.INTER_CUBIC)
        text = pytesseract.image_to_string(res)
        text = text.strip()
        if len(text) > 0:
            print(text)
        break
    cv2.destroyAllWindows()
    return text
    

def lootBoxError():
    str=Check(515, 876, 998, 906)
    if "don't have any lootboxes" in str:
        return True
    else:
        return False
def prayError():
    str=Check(515, 876, 998, 906)
    if "Slow down and try the command again in" in str:
        return True
    else:
        return False
def weaponsCrateError():
    str=Check(515, 876, 998, 906)
    if "don't have any weapon crates" in str:
        return True
    else:
        return False

num=int(input("How many times? "))
commands=["owo lb","owo pray","owo wc"]

test_queue = Deque([-1]*4,maxlen=4) 
    
def randTime():
    y = random.randrange(25)
    return y
open("discord")
time.sleep(15)
pyautogui.click(47, 215)
time.sleep(1)
pyautogui.click(523, 964)
time.sleep(2)
def randCommand():
    for i in range(1, num+1):
        x = random.randrange(3)
        for j in range(4):
            if x == test_queue[j]:
                time.sleep(10)
        test_queue.appendleft(x)
        if(commands[x]=="owo lb" and pair[0][1]==0):
            continue
            
        if(commands[x]=="owo pray" and pair[1][1]==0):
            continue
            
        if(commands[x]=="owo wc" and pair[2][1]==0):
            continue
        
        pyautogui.write(commands[x])
        pyautogui.press('enter')
        time.sleep(1)
        if(lootBoxError()):
                
                pair[0]=("owo lb",0)
                continue
        if(prayError()):
                
                pair[1]=("owo pray",0)
                continue
        if(weaponsCrateError()):
                
                pair[2]=("owo wc",0)
                continue
        time.sleep(randTime())

randCommand()
