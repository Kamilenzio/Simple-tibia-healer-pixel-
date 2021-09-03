from pyautogui import *
from playsound import playsound
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.500)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while True:


    if pyautogui.pixel(1806, 284)[0] == 41 and pyautogui.pixel(249, 805)[0] == 255:

        pyautogui.press('f2')
        time.sleep(0)
        
    if pyautogui.pixel(1841, 286)[0] == 55:
        pyautogui.press('f4')
        time.sleep(0.4)




# 30.08 22:03 dziala

   # if pyautogui.pixel(1806, 284)[0] == 41 and pyautogui.pixel(249, 805)[0] == 255:
#
 #       pyautogui.press('f2')
  #      time.sleep(0.1)
