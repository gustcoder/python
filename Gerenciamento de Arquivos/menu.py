import utils
from bank import db
import operations

def showMenu(account):
    name = db.account_list[account]["name"]
    value = db.account_list[account]["value"]

    utils.printMessage('Bem-vindo, ', name)
    utils.printMessage('Saldo: ', "R$ %s" % utils.formatValue(value))

    print('1: Depositar')
    print('2: Sacar')
    print('3: Sair')

    operation = input("Selecione uma das operações: ")

    operations.doOperations(account, operation)