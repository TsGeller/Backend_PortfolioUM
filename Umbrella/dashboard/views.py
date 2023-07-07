from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Stock , Portfolio , Holder,WalletCashflow
from .forms import StockForm, CashflowForm
from django.urls import reverse 

# Create your views here.
def index (request):
    context = { 
        'wallet':  Portfolio.objects.get(pk=1),
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
    }  

    return HttpResponseRedirect(reverse('dashboard:stocks'),context)

def add(request):
    context = {
        'form': StockForm,
        'formCashflow': CashflowForm,  
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
    } 
    return render(request, 'dashboard/addSomething.html',context)