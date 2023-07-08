class WalletDto:
    def __init__(self, name, stockList, cashflowList, transactionList):
        self.name = name
        self.stockList = stockList
        self.cashflowList = cashflowList
        self.transactionList = transactionList
        ##make getter
    def getName(self):
        return self.name
    def getStockList(self):
        return self.stockList
    def getCashflowList(self):
        return self.cashflowList
    def getTransactionList(self):
        return self.transactionList
    
