class Bank(object): # internamente objetos serao do tipo da classe

    def __init__(self, account):
        self.account = account
        self.__total = 0

    def credit(self, value):
        self.__total += value


    def debit(self, value):
        self.__total -= value
        self.__total -= 1 # desconto de uma taxa


    def getTotal(self):
        return self.__total

