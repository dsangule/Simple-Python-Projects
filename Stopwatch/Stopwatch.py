import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    layout = [
        [sg.Push(), sg.Text('x', enable_events = True, key = '-CLOSE-', pad = (0,0))],
        [sg.VPush()],
        [sg.Text('Time', font = 'Monospace 50', key = '-TIME-')],
        [
            sg.Button(
                'Start', 
                button_color = ('#FFFFFF', '#00FFFF'), 
                border_width = 0, 
                pad = (5,5),
                size = (4,1), 
                key = '-STARTSTOP-'
            ), 
            sg.Button(
                'Lap', 
                button_color = ('#FFFFFF', '#00FFFF'), 
                border_width = 0, 
                pad = (5,5),
                size = (4,1), 
                visible = False,
                key = '-LAP-'
            )
        ],
        [sg.VPush()]
    ]
    return sg.Window('Stopwatch', layout, size = (300, 300), element_justification = 'center', no_titlebar = True)

window = create_window() 
timer_on = 'start'
start_time = 0

while True:
    event, values = window.read(timeout = 10)

    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if timer_on == 'stop':
            timer_on = 'reset'
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible = False)

        elif timer_on == 'start':
            start_time = time()
            timer_on = 'stop'
            window['-STARTSTOP-'].update('Stop')
            window['-LAP-'].update(visible = True)
        
        elif timer_on == 'reset':
            window.close()
            window = create_window()
            timer_on = 'start'
            start_time = 0
    
    if timer_on == 'stop':
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

window.close()