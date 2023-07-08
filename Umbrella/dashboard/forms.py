from django import forms
from .models import Holding, Stock , Portfolio , Holder, WalletCashflow, ActorCashflow

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker','name_stock','type_stock','currency']

class CashflowForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '01/01/1999'}))
    class Meta:
        model = WalletCashflow
        fields = ['date', 'cashflow_entry', 'user_id', 'wallet_id']

class ActorCashflow(forms.ModelForm):
    class Meta:
        model = ActorCashflow
        fields = ['quantity', 'stock_id','price','conversion_rate','price_eur','total_amount','charges','wallet_id','date']

class HoldingForm(forms.ModelForm):
    class Meta : 
        model = Holding
        fields = ['sock_id', 'quantity','wallet_id']
        


