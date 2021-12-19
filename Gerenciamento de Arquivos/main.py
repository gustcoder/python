import getpass
import utils
import operations
from menu import showMenu
from bank import db


def main():
    utils.printMessage('School of Net - Caixa Eletrônico')

    account = input("Digite o número de sua conta: ")

    if account not in db.account_list:
        operations.createNewAccount(account)

    password = getpass.getpass("Digite sua senha: ")

    if operations.authAccount(account, password):
        showMenu(account)
    else:
        print("Senha incorreta")
        exit()


while True:
    main()
    utils.pause()
    utils.clear()