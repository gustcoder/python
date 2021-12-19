import getpass
import utils
from bank import db


def authAccount(account, password):
    if account in db.account_list and password == db.account_list[account]["password"]:
        return True

    return False

def doOperations(account, operation):
    if operation == '1':
        creditOperation(account)

    if operation == '2':
        debitOperation(account)

    if operation == '3':
        exit()

def creditOperation(account):
    credit = float(input("Quanto deseja depositar? "))
    validateCredit(credit)

    db.account_list[account]["value"] += credit
    utils.printMessage('Novo saldo: ', "R$ %s" % utils.formatValue(db.account_list[account]["value"]))    

def debitOperation(account):
    value = db.account_list[account]["value"]
    debit = float(input("Quanto deseja retirar? "))

    validateDebit(debit, value)
        
    db.account_list[account]["value"] -= debit

    moneySlipsOptions = getMoneySlipsOptions(debit)

    if not moneySlipsOptions:
        print("Não temos cédulas!!!")
        exit()

    print('Retire as Cédulas: ', moneySlipsOptions)

    utils.printMessage('Novo saldo:', "R$ %s" % utils.formatValue(db.account_list[account]["value"]))    

def validateCredit(credit):
    if credit <= 0:
        print("Valor inválido!!!")
        exit()

def createNewAccount(account):
    newName = input("Digite o seu nome: ")
    newPassword = getpass.getpass("Digite sua senha: ")
    newValue = input("Deposite valor na conta: ")
    newAccount = {account: {"name": newName, "password": newPassword, "value": newValue}}

    db.account_list.update(newAccount)
    print("Cadastro efetuado com sucesso! Continue para logar...")    

def validateDebit(debit, value):
    if debit > value:
        print("Saldo insuficiente!!!")    
        exit()

def getMoneySlipsOptions(value):
    optionNumber = 0
    numSlipsOptions = {}
    value = int(value)
    for slip in db.money_slips_options:
        optionNumber += 1
        slipInt = int(slip)
        floorValue = value // slipInt

        if floorValue > 0 and floorValue <= db.money_slips_quantity[slip]:
            numSlipsOptions.update({
                slipInt: floorValue
            })
            value = value - (floorValue * slipInt)
            db.money_slips_quantity[slip] -= floorValue

    return numSlipsOptions 