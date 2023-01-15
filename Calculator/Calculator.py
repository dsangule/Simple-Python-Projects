import PySimpleGUI as sg

def create_window(theme):
    
    sg.theme(theme)
    sg.set_options(font = 'Calibri 12')
    button_size = (4,3)

    layout = [
        [
            sg.Text(
                '', 
                font = 'Calibri 24', 
                pad = (10, 20), 
                justification = 'right', 
                expand_x = True,
                right_click_menu = theme_menu,
                key = '-TEXT-'
            )
        ],
        [
            sg.Button('Clear', expand_x = True, size = button_size),
            sg.Button('Enter', expand_x = True, size = button_size)
        ],
        [
            sg.Button('7', size = button_size),
            sg.Button('8', size = button_size),
            sg.Button('9', size = button_size),
            sg.Button('*', size = button_size)
        ],
        [
            sg.Button('4', size = button_size),
            sg.Button('5', size = button_size),
            sg.Button('6', size = button_size),
            sg.Button('/', size = button_size)
        ],
        [
            sg.Button('1', size = button_size),
            sg.Button('2', size = button_size),
            sg.Button('3', size = button_size),
            sg.Button('-', size = button_size)
        ],
        [
            sg.Button('0', expand_x = True, size = button_size),
            sg.Button('.', size = button_size),
            sg.Button('+', size = button_size)
        ]
        
    ]
    
    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['LightGrey1', 'dark', 'DarkGray8', 'random']]
window = create_window('dark')

current_num = []
full_operation = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)

    if event in ['+', '-', '*', '/']:
        full_operation.append(''.join(current_num))
        full_operation.append(event)
        current_num = []
        window['-TEXT-'].update('')

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        ans = eval(''.join(full_operation))
        window['-TEXT-'].update(ans)
        full_operation = []
        current_num = []

    if event == 'Clear':
        window['-TEXT-'].update('')
        full_operation = []
        current_num = []

window.close()