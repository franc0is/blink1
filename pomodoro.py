from lib.blink1_ctypes import Blink1
import time

FOCUS_COLOR = (255, 0, 0)
FOCUS_SECONDS = 25 * 60 # 25 minutes pomodoro

CHILL_COLOR = (0, 255, 0)
CHILL_SECONDS = 5 * 60 # 5 minute rests

DONE_COLOR = (0, 0, 0)

NUM_POMODOROS = 3

def go_chill():
    print("=== TIME TO CHILL ===")
    b.fade_to_rgb(1000, *CHILL_COLOR)

def get_focused():
    print("=== GET TO WORK ===")
    b.fade_to_rgb(1000, *FOCUS_COLOR)

def start_pomodoro():
    get_focused()
    time.sleep(FOCUS_SECONDS)
    go_chill()
    time.sleep(CHILL_SECONDS)

# Init
b = Blink1()
pomodoros = 0

while pomodoros < NUM_POMODOROS:
    start_pomodoro()
    pomodoros = pomodoros + 1

print("=== DONE ===")
b.fade_to_rgb(1000, *DONE_COLOR)

