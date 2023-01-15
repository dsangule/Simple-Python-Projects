import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'), 
        sg.Spin(['sec to min', 'kg to pound', 'km to mile'], key = '-UNITS-'), 
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [
        sg.Text('output', key = '-OUTPUT-')
    ]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'sec to min':
                    output_value = round(float(input_value)/60, 2)
                    output = f'{input_value} seconds in minutes are {output_value} minutes.'

                case 'kg to pound':
                    output_value = round(float(input_value) * 2.20462, 2)
                    output = f'{input_value} kgs in pounds are {output_value} pounds.'
 
                case 'km to mile':
                    output_value = round(float(input_value) * 0.6214, 2)
                    output = f'{input_value} kms in miles are {output_value} miles.'

            window['-OUTPUT-'].update(output)
        else:
            window['-OUTPUT-'].update('Please enter a number.')

window.close()