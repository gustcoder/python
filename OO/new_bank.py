from bank import Bank

class NewBank(Bank):
    def __init__(self, account, cvv):
        #self.account = account ???
        super(NewBank, self).__init__(account)
        self.cvv = cvv

    def debit(self, value):
        self._Bank__total -= value
        self._Bank__total -= 2 # desconto customizado de New Bank de uma taxa
