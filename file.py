import os
import pyautogui
import time

def moyu():
    os.system("powershell -Command taskmgr")
    time.sleep(1)
    pyautogui.keyDown("win")
    time.sleep(0.5)
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.keyUp("win")
