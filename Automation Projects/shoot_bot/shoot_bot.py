from pynput.mouse import Listener
import time

def on_move(x, y):
    mouse_pos=(x, y)
    return mouse_pos

def on_click(x, y, button, pressed):
    press=(x, y, button, pressed)
    return press

def on_scroll(x, y, dx, dy):
    scroll=True


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    print("oi")
    listener.join()
    


x=1
while x==1:
    print(mouse_pos)
    time.sleep(1)







# rom pynput import keyboard
# import time

# break_program = False
# def on_press(key):
#     global break_program
#     print (key)
#     if key == keyboard.Key.end:
#         print ('end pressed')
#         break_program = True
#         return False

# with keyboard.Listener(on_press=on_press) as listener:
#     while break_program == False:
#         print ('program running')
#         time.sleep(5)
#     listener.join()