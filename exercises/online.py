from random import randrange
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

print(screenWidth, screenHeight)

def move_mouse(x = 0, y = 0):
    pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)

while True:
    # move mouse randomly
    time.sleep(5)
    move_mouse(randrange(screenHeight) / 2, randrange(screenWidth) / 2)
    time.sleep(5)

    # execute alt tab
    pyautogui.hotkey('alt', 'tab')
    time.sleep(10)

    # move mouse randomly again
    move_mouse(randrange(screenHeight) / 2, randrange(screenWidth) / 2)
    time.sleep(5)

    # move mouse to center
    move_mouse(0 + (screenWidth / 2), 0 + (screenHeight / 2))
    time.sleep(2)

    # click
    pyautogui.click()

    # input git status
    pyautogui.write('git status', interval=0.15)
    pyautogui.hotkey('enter')
    time.sleep(20)

    # clear terminal
    pyautogui.write('clear', interval=0.15)
    pyautogui.hotkey('enter')
    time.sleep(2)

    pyautogui.write('php artisan clear', interval=0.15)
    pyautogui.hotkey('enter')
    time.sleep(15)

    # clear terminal
    pyautogui.write('clear', interval=0.15)
    pyautogui.hotkey('enter')
    time.sleep(2)

    pyautogui.write('php artisan config:clear', interval=0.15)
    pyautogui.hotkey('enter')
    time.sleep(15)

    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)





