import pyautogui
import time

x=25
y=164
pyautogui.moveTo(x,y,0)
time.sleep(0.5)

while(y<=554):

    while(x<=415):

        pyautogui.moveTo(x,y,0)
        x+=10

        i,j=pyautogui.position()
        if i!=x and j!=y:
            break

    x=25
    y+=10