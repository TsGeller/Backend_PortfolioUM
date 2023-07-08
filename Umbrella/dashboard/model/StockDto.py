class StockDto : 
    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name
        ##self.price = price
        ##make getter 
    def getTicker(self):
        return self.ticker
    def getName(self):
        return self.name
    ##def getPrice(self):
        ##return self.price
    ##make setter
    def setTicker(self, ticker):
        self.ticker = ticker
    def setName(self, name):
        self.name = name
    ##def setPrice(self, price):
        ##self.price = price        
    def __str__(self):
        return f"Ticker: {self.ticker}, Nom: {self.name}"
    def __repr__(self):
        return f"Ticker: {self.ticker}, Nom: {self.name}"
    
    