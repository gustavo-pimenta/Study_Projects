# https://www.youtube.com/watch?v=Et0fYeA2XxY

import PySimpleGUI as sg
import time

sg.theme('DarkAmber')

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Fire Mode:')],
            [sg.Radio('Single Shot','shot', key='single'), sg.Radio('Multiple Shot', 'shot', key='multiple')],
            [],
            [sg.Text('Recoil Size:'), sg.Slider(range=(0, 1000), orientation='h', size=(30, 10), default_value=25, tick_interval=250, key='recoil_size')],
            [],
            [sg.Text('Fire Rate:'), sg.Slider(range=(0, 1000), orientation='h', size=(30, 10), default_value=25, tick_interval=250, key='fire_rate')],
            [],
            [sg.Text('Made by Pimen_Top')]
            
            
            
        ]

        # janela = sg.Window('Shoot Bot').layout(layout)
        janela = sg.Window('Shoot Bot', layout, default_element_size=(400, 10))

        self.button, self.values = janela.Read()
        print(janela.Read())

    def Iniciar(self):

        shot = self.button
        recoil_size = self.values['recoil_size']
        fire_rate = self.values['fire_rate']

        return shot, recoil_size, fire_rate


shot, recoil_size, fire_rate = TelaPython().Iniciar()

while True:
    
    print(shot, recoil_size, fire_rate)
    time.sleep(1)