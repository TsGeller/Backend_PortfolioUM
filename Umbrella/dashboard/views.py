from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock

# Create your views here.
def index (request):
    context = { 
        'stocks': Stock.objects.all() 
    } 
    return render(request, 'dashboard/index.html', context) 

def stock(request):
    context = { 
        'stocks': Stock.objects.all() 
    } 
    return render(request, 'dashboard/stocks.html', context) 