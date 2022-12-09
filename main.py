import PySimpleGUI as sg
import threading
# Define the window's contents

layout = [
    [sg.Button('On', size=(30,19), button_color=('white', 'green'), key='_B_')]
]

# Create the window
window = sg.Window('House Lights', layout).Finalize()
window.maximize()
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    """if event == 'Download':
        True
    if event == 'Create Timecards':
        True
"""

window.close()