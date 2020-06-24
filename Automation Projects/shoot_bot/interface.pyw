# https://www.youtube.com/watch?v=Et0fYeA2XxY

import PySimpleGUI as sg
import time

sg.theme('DarkAmber')

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Fire Mode:')],
            [sg.Radio('Single Shot','shot', key='single', default=True), sg.Radio('Multiple Shot', 'shot', key='multiple', default=False)],  
            [sg.Text('')],
            [sg.Text('Recoil Size:')],
            [sg.Slider(range=(0, 1000), orientation='h', size=(50, 15), default_value=25, tick_interval=250, key='recoil_size')],     
            [sg.Text('')],
            [sg.Text('Fire Rate:')],
            [sg.Slider(range=(0, 1000), orientation='h', size=(50, 15), default_value=25, tick_interval=250, key='fire_rate')],           
            [sg.Text('')],
            [sg.Text('Made by Pimen_Top                                 '), sg.Button('Stop', size=(10,1)), sg.Button('Start', size=(10,1))]
            
            
            
        ]

        # janela = sg.Window('Shoot Bot').layout(layout)
        self.janela = sg.Window('Shoot Bot', layout, default_element_size=(400, 10))
        
        

    def Iniciar(self):
        while True:

            self.button, self.values = self.janela.Read()

            single = self.values['single']
            multiple = self.values['multiple']
            recoil_size = self.values['recoil_size']
            fire_rate = self.values['fire_rate']
            start_stop = self.button

            # return single, multiple, recoil_size, fire_rate, start_stop
            print(single, multiple, recoil_size, fire_rate, start_stop)


TelaPython().Iniciar()

# while True:
    
#     print(shot, recoil_size, fire_rate)
#     time.sleep(1)