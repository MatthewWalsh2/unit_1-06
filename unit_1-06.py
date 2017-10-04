# Created by: Matthew Walsh
# Created on: oct 2017
# Created for: ICS3U
# This program shows the difference between local and global variables

import ui

variableA = 25

def local_variable_button(sender):
    # shows what happen with local variable
    
    variableA = 10
    variableB = 30
    variableC = variableA + variableB
    
    view['local_answer_label'].text = str(variableC)
        
def global_variable_button(sender):
    # shows what happen with global variable
    
    global variableA
    variableA = variableA + 1
    variableB = 30
    variableC = variableA + variableB
    
    view['global_answer_label'].text = str(variableC)

view = ui.load_view()
view.present('full_screen')
