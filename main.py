import pyautogui as pag
import random
import time

while true:
    x = random.randint(1, 1024) 
    y = random.randint(200, 600)
    pag.moveTo(x, y)
    time.sleep(3)    