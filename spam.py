import pyautogui
from AppOpener import open
import time

string=input("Name the app to open : ")
open(string)
for i in range(10):
    pyautogui.write(str(i)+"time spam")
    pyautogui.press('enter')
    time.sleep(2)