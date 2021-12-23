import getpass
import utils
import operations
from menu import showMenu
from bank import db
import generate_bank


def main():
    utils.printMessage('School of Net - Caixa Eletrônico')

    generate_bank.load_bank_data()

    account = input("Digite o número de sua conta: ")

    if account not in db.account_list:
        operations.createNewAccount(account)

    password = getpass.getpass("Digite sua senha: ")

    if operations.authAccount(account, password):
        utils.clear()
        showMenu(account)
        generate_bank.store_bank_data()
    else:
        print("Senha incorreta")
        exit()


while True:
    main()
    utils.pause()
    utils.clear()