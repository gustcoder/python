import os
from posixpath import split
import utils
from bank import db


def open_bank_file(mode, file):
    return open(os.path.abspath(file), mode)    

# gera no formado cedula=valor; Ex.: 100=5;50=2;20=3;
def store_money_slips(mode):
    file = open_bank_file(mode, './bank/_money_slips.dat')

    for key, value in db.money_slips_options.items():
        file.write(key+'='+str(value)+';')

    file.write('\n')
    file.close()


def read_money_slips():
    file = open_bank_file('r', './bank/_money_slips.dat')

    lines = file.readlines()

    for line in lines:
        items = line.split(';')
        set_money_slips(items)


def set_money_slips(list_money_slips):
    for item in list_money_slips:
        slip = item.split('=')
        if slip != [''] and slip != ['\n']:
            money_bill = slip[0]
            money_value = int(slip[1])

            db.money_slips_options[money_bill] = money_value


# gera no formado cedula=valor; Ex.: 100=5;50=2;20=3;
def store_money_slips_quantity(mode):
    file = open_bank_file(mode, './bank/_money_slips_quantity.dat')

    for key, value in db.money_slips_quantity.items():
        file.write(key+'='+str(value)+';')

    file.write('\n')
    file.close()    


def read_money_slips_quantity():
    file = open_bank_file('r', './bank/_money_slips_quantity.dat')

    lines = file.readlines()

    for line in lines:
        items = line.split(';')
        set_money_slips_quantity(items)


def set_money_slips_quantity(list_money_slips_quantity):
    for item in list_money_slips_quantity:
        slip = item.split('=')
        if slip != [''] and slip != ['\n']:
            money_bill = slip[0]
            money_value = int(slip[1])

            db.money_slips_quantity[money_bill] = money_value            


# gera no formado cedula=valor; Ex.: 100=5;50=2;20=3;
def store_accounts(mode):
    file = open_bank_file(mode, './bank/_accounts.dat')

    accounts = db.account_list
    for key, value in accounts.items():
        file.write('account_number='+key+';')
        file.write('name='+value['name']+';')
        file.write('password='+value['password']+';')
        file.write('value='+str(value['value'])+';')
        file.write('\n')

    file.close()            


def read_accounts():
    file = open_bank_file('r', './bank/_accounts.dat')

    lines = file.readlines()

    for line in lines:
        items = line.split(';')
        set_accounts(items)


def set_accounts(accounts_list):
    if accounts_list != ['\n']:
        account_number = accounts_list[0].split('=')[1]
        account_name = accounts_list[1].split('=')[1]
        account_password = accounts_list[2].split('=')[1]
        account_value = accounts_list[3].split('=')[1]

        account_data = {
            'name': account_name,
            'password': account_password,
            'value': float(account_value)
        }

        db.account_list[account_number] = account_data


def load_bank_data():
    read_money_slips()
    read_money_slips_quantity()
    read_accounts()

def store_bank_data():
    store_money_slips('w')
    store_money_slips_quantity('w')
    store_accounts('w')
