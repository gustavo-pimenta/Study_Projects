import pyautogui
import time

print('ESCOLHA UM NUMERO PARA REPETIÇÃO: ')
num=int(input())
cont=7

print('\n\nCONTAGEM REGRESSIVA, SELECIONE A CAIXA DE TEXTO: ')

while cont>0:
    print(cont)
    cont-=1
    time.sleep(1)

while cont<num:
    pyautogui.typewrite('Amor')
    pyautogui.press('enter')
    cont+=1



