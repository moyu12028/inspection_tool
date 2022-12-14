import os
import pyautogui
import time
import win32gui


def idou():
    time.sleep(3)
    memoapp = win32gui.FindWindow(None,'タスク マネージャー')
    time.sleep(1)
    #win32gui.SetForegroundWindow(memoapp)``
    time.sleep(1)
    pyautogui.hotkey("win","up","left")
    print("nonononono")