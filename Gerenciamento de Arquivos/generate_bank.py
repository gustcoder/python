import os
from posixpath import split
import utils
from bank import db

def main():
    utils.printMessage('School of Net - Caixa Eletrônico')
    utils.printMessage('Gerando cédulas...')
    generate_money_slips()
    read_money_slips()

def open_bank_file(mode):
    return open(os.path.abspath('./_bank.dat'), mode)    

# gera no formado cedula=valor; Ex.: 100=5;50=2;20=3;
def generate_money_slips():
    file = open_bank_file('w')

    money_slips = db.money_slips_options
    for key, value in money_slips.items():
        file.write(key+'='+str(value)+';')

    file.close()
    utils.printMessage('Cédulas geradas com sucesso!!!')

def read_money_slips():
    file = open_bank_file('r')

    lines = file.readlines()

    for line in lines:
        items = line.split(';')
        set_money_slips(items)

def set_money_slips(list_money_slips):
    for item in list_money_slips:
        slip = item.split('=')
        if slip != ['']:
            money_bill = slip[0]
            money_value = int(slip[1])

            db.money_slips_options[money_bill] = money_value


main()