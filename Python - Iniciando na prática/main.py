import getpass
import os


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

money_slips = {
    '100': 100,
    '50': 50,
    '20': 20,
    '10': 10,
    '5': 5
}

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

def _buildNumSlipsOptions(optionNumber, value, slip):
    modSlips = float(value) % float(slip)
    if (modSlips == 0):
        numSlips = int(float(value) / float(slip))
        numSlipsOptions = {
            str(optionNumber): str(numSlips) + " cédulas de " + slip
        }

        return numSlipsOptions
    else:
        print("Opção inválida!!!")

def buildNumSlipsOptions(optionNumber, value, slip):
    if value // slip > 0:
        numSlipsOptions = {
            slip: value // slip
        }
        buildNumSlipsOptions(optionNumber, value, slip)

def getMoneySlipsOptions(value):
    optionNumber = 0
    numSlipsOptions = {}
    value = int(value)
    for slip in money_slips:
        optionNumber += 1
        slip = int(slip)

        if value // slip > 0:
            numSlipsOptions.update({
                slip: value // slip
            })
            value = value - value // slip * slip

    return numSlipsOptions


while True:
    print('****************************************')
    print('*** School of Net - Caixa Eletrônico ***')
    print('****************************************')

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

        print('1: Depositar')
        print('2: Sacar')
        print('3: Sair')

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

            moneySlipsOptions = getMoneySlipsOptions(debit)

            if not moneySlipsOptions:
                print("Não temos cédulas!!!")
                exit()

            print('Retire as Cédulas: ', moneySlipsOptions)

            print('________________________________________')
            print("Novo saldo: R$ %s" % formatValue(account_list[account]["value"]))
        elif option == '3':
            exit()
    else:
        print("Senha incorreta")