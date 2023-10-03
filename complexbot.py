import time
import random
from typing import Deque
import pyautogui
from AppOpener import open
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
import threading

reset_thread = None
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
pair=[("owo h",1),
    ("owo b",1),
    ("owo pray",1),
    ("owo inv",1),
    ("owo wc",1),
    ("owo z",1),
    ("owo cash",1),
    ("owo q",1),
    ("owo cl",1),
    ("owo pika",1),
    ("owo lb",1),
    ("owo w",1)]

def Check(x1,y1,x2,y2): #checking using tesseract inside the box
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
    
def checkBan(): #checking ban
    str=Check(515, 876, 998, 906)
    if "owobot.com/captcha" in str:
        return True
    else:
        return False

def lootBoxError(): #checking lootbox error
    str=Check(515, 876, 998, 906)
    if "don't have any lootboxes" in str:
        return True
    else:
        return False

def weaponsCrateError(): #checking weapon crate error
    str=Check(515, 876, 998, 906)
    if "don't have any weapon crates" in str:
        return True
    else:
        return False
    
def receivedLootbox(): #checking if lootbox is received
    str=Check(515, 876, 998, 906)
    if "found a lootbox" in str:
        return True
    else:
        return False
    
def receivedWeaponsCrate(): #checking if weapon crate is received
    str=Check(515, 876, 998, 906)
    if "found a weapon crate" in str:
        return True
    else:
        return False
    
def reset_pray_flag(): #resetting pray flag after 5 minutes
    while True:
        time.sleep(300)  
        pair[2] = ("owo pray", 1)
        print("Resetting 'pair[2]' to ('owo pray', 1)")
       
num=int(input("How many times? "))
commands=["owo lb","owo h","owo b","owo inv","owo h","owo b","owo wc","owo h","owo b","owo z","owo cash","owo q","owo cl","owo b","owo pika","owo army","owo w","owo h"]
pray = "owo pray"
test_queue = Deque([-1]*4,maxlen=4) 
    
def randTime(): #random time
    y = random.randrange(25)
    return y

def prayCommand(): #pray command  
        time.sleep(3)
        while True:
            if pair[2][1] == 1:  # Check if the flag is set to 1
                pyautogui.write(pray)
                pyautogui.press('enter')
                pair[2] = ("owo pray", 0)
                time.sleep(1)
                if checkBan():
                    print("Banned")
                    exit()
            time.sleep(1)

reset_thread = threading.Thread(target=reset_pray_flag)
pray_thread = threading.Thread(target=prayCommand)

open("discord")
time.sleep(15)
pyautogui.click(47, 215)
time.sleep(1)
pyautogui.click(523, 964)
time.sleep(2)

pray_thread.start()
time.sleep(5)
reset_thread.start()

def randCommand():  #random command
    global reset_thread
    for i in range(1, num+1):
        x = random.randrange(18)
        for j in range(4):
            if x == test_queue[j]:
                time.sleep(10)
        test_queue.appendleft(x)
        if(commands[x]=="owo lb" and pair[10][1]==0):
            continue
            
        if(commands[x]=="owo wc" and pair[4][1]==0):
            continue

        pyautogui.write(commands[x])
        pyautogui.press('enter')
        time.sleep(1)
        if(lootBoxError()):
                pair[10]=("owo lb",0)
                continue
        if(weaponsCrateError()):
                pair[4]=("owo wc",0)
                continue
        if(receivedLootbox()):  
                pair[10]=("owo lb",1)
                continue
        if(receivedWeaponsCrate()):
                pair[4]=("owo wc",1)
                continue
        if(checkBan()):
                print("Banned")
                exit()
        time.sleep(randTime())
        
        i+=1



randCommand()


