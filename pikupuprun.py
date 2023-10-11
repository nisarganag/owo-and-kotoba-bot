import sys
import time
import pyautogui
from AppOpener import open

num=int(input("How many times? "))

open("discord")
time.sleep(15)
pyautogui.click(47, 215)
time.sleep(1)
pyautogui.click(523, 964)
time.sleep(2)

for i in range(1, num+1):
    pyautogui.write("owo piku")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write("owo pup")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write("owo run")
    pyautogui.press('enter')
    time.sleep(60)
    i+=1
sys.exit()