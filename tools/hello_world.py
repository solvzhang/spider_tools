
import PySimpleGUI as sg


text = sg.Text("Hello:")
text_entry = sg.InputText()
layout = [[text, text_entry]]


window = sg.Window('Hello World', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break


window.close()