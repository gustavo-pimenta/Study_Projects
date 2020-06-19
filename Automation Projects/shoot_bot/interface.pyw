import PySimpleGUI as sg
import time

class Tela:
    def __init__(self):
        layout = [
            [sg.Text('teste')]
            [sg.Input()]
            [sg.Button('Start')]
            [sg.Button('Stop')]
        ]

        janela = sg.Window('Shoot Bot').layout(layout)

        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

Tela.iniciar()
        
