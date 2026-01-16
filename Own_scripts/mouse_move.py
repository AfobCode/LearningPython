import pyautogui
import time
from datetime import datetime, timedelta

def movemente(t=5):
    #t = t*60
    time.sleep(t)
    current_x, current_y = pyautogui.position()
    print(current_x,current_y)

    # 1. move the mouse 100 pixels to the right
    pyautogui.moveTo(current_x + 100,current_y,duration=0.5)
    time.sleep(t)
    # 2. move the mouse 50 pixels down
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x,current_y-50,duration=0.5)
    time.sleep(t)
    # 3. move the mouse 100 pixels to the left
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x - 100,current_y,duration=0.5)
    time.sleep(t)
    # 4. move the mouse 50 pixels up
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x,current_y+50,duration=0.5)
    time.sleep(t)

    pyautogui.click()


def time_to_move(time_move,loop_time):
    now = datetime.now()
    end = now + timedelta(minutes=loop_time)
    time_move = time_move *60

    while now < end:
        time.sleep(time_move)
        now = datetime.now()
        print(now)
        print(end)
        movemente()
        


time_to_move(4.5,150)