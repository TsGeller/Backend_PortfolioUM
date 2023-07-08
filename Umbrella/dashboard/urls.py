from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('stocks/', views.stocks, name='stocks'),
    path('addstock/', views.addstock, name='addstock'),
    path('add/', views.add, name='add'),
    path('addCashflow/', views.addCashflow, name='addCashflow'),
    path('addTransaction/', views.addTransaction, name='addTransaction'),
    path('addhold/', views.addhold, name='addhold'),
]
