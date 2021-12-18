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

money_slips_options = {
    '100': 100,
    '50': 50,
    '20': 20,
    '10': 10,
    '5': 5
}

money_slips_quantity = {
    '100': 10,
    '50': 20,
    '20': 30,
    '10': 40,
    '5': 50
}

def main():
    printMessage('School of Net - Caixa Eletrônico')

    account = input("Digite o número de sua conta: ")

    if account not in account_list:
        createNewAccount(account)

    password = getpass.getpass("Digite sua senha: ")

    if authAccount(account, password):
        showMenu(account)
    else:
        print("Senha incorreta")
        exit()

def pause():
    input('Pression <ENTER> para continuar...')

def authAccount(account, password):
    if account in account_list and password == account_list[account]["password"]:
        return True
    return False

def showMenu(account):
    name = account_list[account]["name"]
    value = account_list[account]["value"]

    printMessage('Bem-vindo, ', name)
    printMessage('Saldo: ', "R$ %s" % formatValue(value))

    print('1: Depositar')
    print('2: Sacar')
    print('3: Sair')

    operation = input("Selecione uma das operações: ")

    doOperations(account, operation)

def doOperations(account, operation):
    if operation == '1':
        creditOperation(account)

    if operation == '2':
        debitOperation(account)

    elif operation == '3':
        exit()

def creditOperation(account):
    credit = float(input("Quanto deseja depositar? "))
    validateCredit(credit)

    account_list[account]["value"] += credit
    printMessage('Novo saldo: ', "R$ %s" % formatValue(account_list[account]["value"]))    

def debitOperation(account):
    value = account_list[account]["value"]
    debit = float(input("Quanto deseja retirar? "))

    validateDebit(debit, value)
        
    account_list[account]["value"] -= debit

    moneySlipsOptions = getMoneySlipsOptions(debit)

    if not moneySlipsOptions:
        print("Não temos cédulas!!!")
        exit()

    print('Retire as Cédulas: ', moneySlipsOptions)

    printMessage('Novo saldo:', "R$ %s" % formatValue(account_list[account]["value"]))    

def formatValue(value):
    return str(float(value))

def validateCredit(credit):
    if credit <= 0:
        print("Valor inválido!!!")
        exit()

def clear():
    os.system('cls' if os.name == "nt" else 'clear')

def createNewAccount(account):
    newName = input("Digite o seu nome: ")
    newPassword = getpass.getpass("Digite sua senha: ")
    newValue = input("Deposite valor na conta: ")
    newAccount = {account: {"name": newName, "password": newPassword, "value": newValue}}

    account_list.update(newAccount)
    print("Cadastro efetuado com sucesso! Continue para logar...")    

def validateDebit(debit, value):
    if debit > value:
        print("Saldo insuficiente!!!")    
        exit()

def getMoneySlipsOptions(value):
    optionNumber = 0
    numSlipsOptions = {}
    value = int(value)
    for slip in money_slips_options:
        optionNumber += 1
        slipInt = int(slip)
        floorValue = value // slipInt

        if floorValue > 0 and floorValue <= money_slips_quantity[slip]:
            numSlipsOptions.update({
                slipInt: floorValue
            })
            value = value - (floorValue * slipInt)
            money_slips_quantity[slip] -= floorValue

    return numSlipsOptions

def printMessage(text, value = ''):    
    print(text + " " + value)
    print('****************************************')        

while True:
    main()

    pause()

    clear()