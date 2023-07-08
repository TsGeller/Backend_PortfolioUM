class WalletDto:
    def __init__(self, name, stockList, cashflowList, transactionList):
        self.name = name
        self.stockList = stockList
        self.cashflowList = cashflowList
        self.transactionList = transactionList
    def __init__(self):
        self.name = ""
        self.stockList = []
        self.cashflowList = []
        self.transactionList = []
        ##make getter
    def getName(self):
        return self.name
    def getStockList(self):
        return self.stockList
    def getCashflowList(self):
        return self.cashflowList
    def getTransactionList(self):
        return self.transactionList
    ## make setter
    def setName(self,name):
        self.name= name
    def setStockList(self, stockList):
        self.stockList = stockList
    def setCashflowList(self,cashflowList):
        self.cashflowList = cashflowList
    ##make tostring
    def __str__(self):  
        return f"WalletDto: {self.name}, {self.stockList}, {self.cashflowList}, {self.transactionList}"
    
