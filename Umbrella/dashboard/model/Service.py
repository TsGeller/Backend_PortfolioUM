from ..models import Holding, Portfolio
import pandas as pd

class Service:
    ##walletDto = WalletDto("Umbrella", [], [], [])
    
    def __init__(self,hold):
        portfolio = Portfolio.objects.get(name = hold)
        cashflowList = []
        print(portfolio)
        queryset = Holding.objects.filter(wallet_id = portfolio)
        nameWallet = "Umbrella"
        print("quoicoubeh")
        ##########
        print("queryset panda")
        pd.set_option('display.max_colwidth', None)
        data = list(queryset.values())
        df = pd.DataFrame(data)
        print(df)
        print("queryset panda")
        ######## 
        print(hold) 
        holding  = []      
        for hold in queryset:
            holding.append(hold)
        print(holding)
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print(df)
         
        
    
