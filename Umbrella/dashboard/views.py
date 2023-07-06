from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock , Portfolio , Holder,WalletCashflow

# Create your views here.
def index (request):
    context = { 
        'wallet':  Portfolio.objects.get(pk=1),
        'cashflows': WalletCashflow.objects.all()
    } 
    return render(request, 'dashboard/index.html', context) 

def stock(request):
    context = { 
        'stocks': Stock.objects.all() 
    } 
    return render(request, 'dashboard/stocks.html', context) 