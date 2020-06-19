# import pyautogui
from pynput import mouse
import time

# pyautogui.FAILSAFE = True 


# def on_click(x, y, button, pressed):
#     x=('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
#     # Stop listener
#     # if not pressed:
#     #     return False

# Collect events until released
# with mouse.Listener(on_click=on_click,) as listener:
#     listener.join()

with mouse.Listener() as listener:
    listener.join()

listener.start()
        



# def main():

while True:

    print(x)

    with mouse.Events() as events:
        for event in events:
            if event.button == mouse.Button.left:
                break
            else:
                print('Received event {}'.format(event))

    time.sleep(1)

   
# if __name__ == "__main__":
#     main()