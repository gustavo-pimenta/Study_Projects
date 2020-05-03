# pyautogui.position()
# pyautogui.moveTo(x,y,duration)
# pyautogui.click(x,y)
# pyautogui.doubleClick(x,y)
# pyautogui.rightClick(x,y)
# pyautogui.hotkey(‘Ctrl’,’Shift’,’q’)
# Pyautogui.KEYBOARD_KEYS
# pyautogui.press('enter')

import pyautogui
import time

print('ESCOLHA UM NUMERO PARA REPETIÇÃO DESSA PRAGA: ')
num=int(input())

# elefante=1
# elefante_mais=2
cont=7

print('\n\nCONTAGEM REGRESSIVA, SELECIONE A CAIXA DE TEXTO: ')

while cont>0:

    print(cont)
    cont-=1
    time.sleep(1)

while cont<num:
    
    # if(elefante==1):
    #     elefante=str(elefante)
    #     elefante_mais=str(elefante_mais)
    #     texto=elefante+' ELEFANTE INCOMODA MUITA GENTE, '+elefante_mais+' ELEFANTES INCOMODAM MUITO MAIS'
    #     elefante=int(elefante)
    #     elefante_mais=int(elefante_mais)
    # else:
    #     elefante=str(elefante)
    #     elefante_mais=str(elefante_mais)
    #     texto=elefante+' ELEFANTES INCOMODAM MUITA GENTE, '+elefante_mais+' ELEFANTES INCOMODAM MUITO MAIS'
    #     elefante=int(elefante)
    #     elefante_mais=int(elefante_mais)


    pyautogui.typewrite('Amor')
    pyautogui.press('enter')
    # time.sleep(0.01)

    # elefante+=1
    # elefante_mais+=1
    cont+=1



