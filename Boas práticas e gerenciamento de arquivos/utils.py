import os


def printMessage(text, value = ''):    
    print(text + " " + value)
    print('****************************************')


def pause():
    input('Pression <ENTER> para continuar...')    


def clear():
    os.system('cls' if os.name == "nt" else 'clear')    


def formatValue(value):
    return str(float(value))    