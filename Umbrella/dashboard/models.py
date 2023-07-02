from django.contrib.auth.models import AbstractUser 
from django.db import models

# Create your models here.
class Holder(AbstractUser):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)    
    value_lastDay = models.DecimalField(max_digits=10, decimal_places=2)
    value_today = models.DecimalField(max_digits=10, decimal_places=2)

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=10)
    name_stock = models.CharField(max_length=200)
    type_stock = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)

class Holding(models.Model):
    id = models.AutoField(primary_key=True)
    sock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    wallet_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

class ActorCashflow(models.Model):
    id = models.AutoField(primary_key=True) 
    quantity = models.IntegerField()
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=2)
    price_eur = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    wallet_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE) 
    date = models.DateField()

class WalletCashflow(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    cashflow_entry = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(Holder, on_delete=models.CASCADE)
    wallet_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

