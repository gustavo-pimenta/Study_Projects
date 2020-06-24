# https://www.youtube.com/watch?v=Et0fYeA2XxY

import PySimpleGUI as sg
import time

sg.theme('DarkAmber')

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Button('Single Shot', size=(20, 1)),sg.Button('Multiple Shot', size=(20, 1))],
            [],
            [sg.Text('Recoil Size:'), sg.Slider(range=(0, 1000), orientation='h', size=(30, 10), default_value=25, tick_interval=250)],
            [],
            [sg.Text('Fire Rate:'), sg.Slider(range=(0, 1000), orientation='h', size=(30, 10), default_value=25, tick_interval=250)],
            [],
            [sg.Text('Made by Pimen_Top')]
            
            
            
        ]

        # janela = sg.Window('Shoot Bot').layout(layout)
        janela = sg.Window('Shoot Bot', layout, default_element_size=(400, 10))

        self.button, self.values = janela.Read()

def Iniciar(self):
    print(self.values)

# tela = 
TelaPython().Iniciar()
        
