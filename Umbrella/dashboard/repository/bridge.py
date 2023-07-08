import yfinance as yf
##class who make call api yfinance
class Bridge:
    ## get the price of a stock with a ticker in parameter
    def getpriceofStock(self, stock):
        return 