import pyautogui, time

while True:
    x,y=pyautogui.position()
    pyautogui.click(x,y)
    time.sleep(2)
