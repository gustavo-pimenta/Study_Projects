# https://www.youtube.com/watch?v=Et0fYeA2XxY

import PySimpleGUI as sg
import time

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('teste')],
            [sg.Input()],
            [sg.Button('Start')],
            [sg.Button('Stop')]
        ]

        janela = sg.Window('Shoot Bot').layout(layout)

        self.button, self.values = janela.Read()

def Iniciar(self):
    print(self.values)

# tela = 
TelaPython().Iniciar()
        
