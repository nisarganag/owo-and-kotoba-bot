import time
import random
from typing import Deque
import pyautogui
from AppOpener import open
# import cv2
# import numpy as np
# import pytesseract
# from PIL import ImageGrab
import threading
reset_thread = None
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
pair=[("owo pray",1),("owo h",1)
    ]
# def Check(x1,y1,x2,y2):
#     while True:
#         cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))
#         cap_arr = np.array(cap)
#         res=cv2.resize(cap_arr,None,fx=1,fy=1,interpolation=cv2.INTER_CUBIC)
#         text = pytesseract.image_to_string(res)
#         text = text.strip()
#         if len(text) > 0:
#             print(text)
#         break
#     cv2.destroyAllWindows()
#     return text
    

# def lootBoxError():
#     str=Check(515, 876, 998, 906)
#     if "don't have any lootboxes" in str:
#         return True
#     else:
#         return False
# def weaponsCrateError():
#     str=Check(515, 876, 998, 906)
#     if "don't have any weapon crates" in str:
#         return True
#     else:
#         return False
# def receivedLootbox():
#     str=Check(515, 876, 998, 906)
#     if "found a lootbox" in str:
#         return True
#     else:
#         return False
# def receivedWeaponsCrate():
#     str=Check(515, 876, 998, 906)
#     if "found a weapon crate" in str:
#         return True
#     else:
#         return False
def reset_pray_flag():
    while True:
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)
        pair[0] = ("owo pray", 1)
        print("Resetting 'pair[0]' to ('owo pray', 1)")
        print("pair[0] = ", pair[0])
       
num=int(input("How many times? "))
commands=["owo pray","owo h"]

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
    global reset_thread
    for i in range(1, num+1):
        x = random.randrange(2)
        for j in range(4):
            if x == test_queue[j]:
                time.sleep(10)
        test_queue.appendleft(x)
        # if(commands[x]=="owo lb" and pair[10][1]==0):
        #     continue
        print("i = ", i, "Command = ", commands[x])   
        if(commands[x]=="owo pray" and pair[0][1]==0):
            continue
            
        # if(commands[x]=="owo wc" and pair[4][1]==0):
        #     continue
        
        if(commands[x]=="owo pray" and pair[0][1]==1):
            pair[0]=("owo pray",0)
            print("pair[0] = ", pair[0])
            if reset_thread and reset_thread.is_alive():
                reset_thread.join()
            reset_thread = threading.Thread(target=reset_pray_flag)
            reset_thread.start() 
        
        pyautogui.write(commands[x])
        pyautogui.press('enter')
        time.sleep(1)
        # if(lootBoxError()):
        #         pair[10]=("owo lb",0)
        #         continue
        # if(weaponsCrateError()):
        #         pair[4]=("owo wc",0)
        #         continue
        # if(receivedLootbox()):  
        #         pair[10]=("owo lb",1)
        #         continue
        # if(receivedWeaponsCrate()):
        #         pair[4]=("owo wc",1)
        #         continue
        time.sleep(randTime())
        i+=1
        
randCommand()

