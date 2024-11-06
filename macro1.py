import pyautogui
import time

time.sleep(5)

interval1 = 5
interval2 = 0.5

while True:
    pyautogui.press('F2')
    time.sleep(interval2)
    pyautogui.press('enter')
    time.sleep(interval1)
