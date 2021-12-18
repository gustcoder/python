import getpass
import os


def formatValue(value):
    return str(float(value))

def validateCredit(credit):
    if credit <= 0:
        print("Valor inválido!!!")
        exit()

def clear():
    os.system('cls' if os.name == "nt" else 'clear')

def validateDebit(debit, value):
    if debit > value:
        print("Saldo insuficiente!!!")    
        exit()


while True:
    print('****************************************')
    print('*** School of Net - Caixa Eletrônico ***')
    print('****************************************')

    account_list = {
        "001": {
            "name": "Gustavo",
            "password": "321",
            "value": 5000
        },
        "002": {
            "name": "Phil",
            "password": "456789",
            "value": 4600
        },
        "003": {
            "name": "Sueli",
            "password": "123456",
            "value": 8000
        }
    }

    account = input("Digite o número de sua conta: ")

    if account not in account_list:
        clear()
        newName = input("Digite o seu nome: ")
        newPassword = getpass.getpass("Digite sua senha: ")
        newValue = input("Deposite valor na conta: ")
        newAccount = {account: {"name": newName, "password": newPassword, "value": newValue}}

        account_list.update(newAccount)
        print("Cadastro efetuado com sucesso! Continue para logar...")

    password = getpass.getpass("Digite sua senha: ")

    if account in account_list and password == account_list[account]["password"]:
        name = account_list[account]["name"]
        value = account_list[account]["value"]

        print('****************************************')
        print("Bem-vindo, " + name)
        print('****************************************')
        print("Saldo: R$ %s" % formatValue(value))
        print('****************************************')

        print('1 - Depositar')
        print('2 - Sacar')
        print('3 - Sair')

        option = input("Digite uma das opções: ")

        clear()

        if option == '1':
            credit = float(input("Quanto deseja depositar? "))
            validateCredit(credit)

            account_list[account]["value"] += credit
            print('****************************************')
            print("Novo saldo: R$ %s" % formatValue(account_list[account]["value"]))
            print('****************************************')
        if option == '2':
            debit = float(input("Quanto deseja retirar? "))
            validateDebit(debit, value)
                
            account_list[account]["value"] -= debit
            print('****************************************')
            print("Novo saldo: R$ %s" % formatValue(account_list[account]["value"]))
            print('****************************************')
        elif option == '3':
            exit()
    else:
        print("Senha incorreta")