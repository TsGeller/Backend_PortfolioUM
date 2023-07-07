from django import forms
from .models import Stock , Portfolio , Holder,WalletCashflow

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker','name_stock','type_stock','currency']
class CashflowForm(forms.ModelForm):
    class Meta:
        model = WalletCashflow
        fields = ['date','cashflow_entry','user_id','wallet_id']
        


