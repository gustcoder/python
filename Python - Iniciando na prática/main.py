import getpass


def formatValue(value):
    return str(float(value))

print('****************************************')
print('*** School of Net - Caixa Eletrônico ***')
print('****************************************')

account_list = {
    "00001-01": {
        "name": "Gustavo",
        "password": "321",
        "value": 5000
    },
    "00002-01": {
        "name": "Phil",
        "password": "456789",
        "value": 4600
    },
    "00003-01": {
        "name": "Sueli",
        "password": "123456",
        "value": 8000
    }
}

account = input("Digite o número de sua conta: ")

if account not in account_list:
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
    print("Bem-vindo, " + name)
    print("Saldo: R$" + formatValue(value))
    exit()

print("Senha incorreta")