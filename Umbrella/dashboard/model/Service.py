
from .WalletDto import WalletDto
from ..models import Holding, Portfolio, WalletCashflow
import pandas as pd

class Service:
    walletDto = WalletDto()
    
    def __init__(self,hold):
        portfolio = Portfolio.objects.get(name = hold)        
        querysetstocklist = Holding.objects.filter(wallet_id = portfolio) 
        querysetWalletCashflow = WalletCashflow.objects.filter(wallet_id = portfolio) 
        ##########
        print("queryset for stockList")        
        data = list(querysetstocklist.values())
        stocklist = pd.DataFrame(data)
               
        ########
        ##########
        print("queryset for Cashflow List")        
        data = list(querysetWalletCashflow.values())
        WalletCashflows = pd.DataFrame(data)
               
        ######## 
        
        self.walletDto.name = hold
        self.walletDto.cashflowList = WalletCashflows
        self.walletDto.stockList = stocklist
    def getWalletDto(self):
        return self.walletDto
    ##make tostring 
    def __str__(self):
        return f"WalletDto: {self.walletDto}"
         
        
    
