from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Holding, Stock , Portfolio ,WalletCashflow
from .forms import ActorCashflow, HoldingForm, StockForm, CashflowForm
from django.urls import reverse 
from .model.Service import Service


# Create your views here.
def index (request):
    hold = "Umbrella"
    service = Service(hold) 
    print("print ici")
    print(service.getWalletDto())  
    context = {  
        'wallet':  Holding.objects.filter(wallet_id = 1),       
        ##'wallet':  service.walletDto.getStockList(), 
        'cashflows': WalletCashflow.objects.all()   
    } 
    return render(request, 'dashboard/index.html', context) 

def stocks(request):
    context = { 
        'stocks': Stock.objects.all() 
    } 
    return render(request, 'dashboard/stocks.html', context) 

def addstock(request):
    form = StockForm(request.POST)
    if form.is_valid():
        Stock.objects.create(    
        ticker = form.cleaned_data['ticker'],  
        name_stock = form.cleaned_data['name_stock'], 
        type_stock = form.cleaned_data['type_stock'], 
        currency = form.cleaned_data['currency'] 
        )
        context = {
        'form': StockForm,
        'formCashflow': CashflowForm,
        'formTransaction': ActorCashflow,  
        'holdingForm': HoldingForm, 
    }  

    return HttpResponseRedirect(reverse('dashboard:stocks'),context)

def add(request):
    context = {
        'form': StockForm,
        'formCashflow': CashflowForm, 
        'formTransaction': ActorCashflow,
        'holdingForm': HoldingForm, 
    }    
    return render(request, 'dashboard/addSomething.html',context)

def addCashflow(request):
    cashflowForm = CashflowForm(request.POST)
    if cashflowForm.is_valid():
        WalletCashflow.objects.create(    
        date = cashflowForm.cleaned_data['date'],  
        cashflow_entry = cashflowForm.cleaned_data['cashflow_entry'], 
        user_id = cashflowForm.cleaned_data['user_id'], 
        wallet_id = cashflowForm.cleaned_data['wallet_id'] 
        )
        context = {
        'form': StockForm,
        'formCashflow': CashflowForm,  
        'formTransaction': ActorCashflow,
        'holdingForm': HoldingForm,
    } 
    return render(request, 'dashboard/addSomething.html',context)

def addTransaction(request):
    transactionForm = ActorCashflow(request.POST)
    if transactionForm.is_valid():
        ActorCashflow.objects.create(    
        quantity = transactionForm.cleaned_data['quantity'],  
        stock_id = transactionForm.cleaned_data['stock_id'], 
        price = transactionForm.cleaned_data['price'], 
        conversion_rate = transactionForm.cleaned_data['conversion_rate'],
        price_eur = transactionForm.cleaned_data['price_eur'],
        total_amount = transactionForm.cleaned_data['total_amount'],
        charges = transactionForm.cleaned_data['charges'],
        wallet_id = transactionForm.cleaned_data['wallet_id'],
        date = transactionForm.cleaned_data['date'] 
        )
        
    context = {
        'form': StockForm,
        'formCashflow': CashflowForm, 
        'formTransaction': ActorCashflow,
        'HoldingForm': HoldingForm,
    }    
    return render(request, 'dashboard/addSomething.html',context)
def addhold(request):
    holdingForm = HoldingForm(request.POST)
    if holdingForm.is_valid():
        Holding.objects.create(    
        sock_id = holdingForm.cleaned_data['sock_id'],  
        quantity = holdingForm.cleaned_data['quantity'], 
        wallet_id = holdingForm.cleaned_data['wallet_id'], 
        )
    context = {
        'form': StockForm,
        'formCashflow': CashflowForm, 
        'formTransaction': ActorCashflow,
        'HoldingForm': HoldingForm,
    }  
    return render(request, 'dashboard/addSomething.html',context)

def page404(request, exception):
    return render(request, 'app/404.html')
