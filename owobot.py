import time
import random
from typing import Deque
import pyautogui
from AppOpener import open

  
num=int(input("How many times? "))
commands=["owo lb","owo b","owo pray","owo inv","owo h","owo wc","owo z","owo cash","owo q","owo cl","owo pika","owo army","owo w"]

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
        x = random.randrange(13)
        for j in range(4):
            if x == test_queue[j]:
                time.sleep(10)
        test_queue.appendleft(x)
        pyautogui.write(commands[x])
        pyautogui.press('enter')
        time.sleep(randTime())

randCommand()

