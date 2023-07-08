from django.contrib.auth.models import AbstractUser 
from django.db import models

class Holder(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f"Nom d'utilisateur: {self.user_name}"

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    value_lastDay = models.DecimalField(max_digits=10, decimal_places=2)
    value_today = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nom: {self.name}"

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=10)
    name_stock = models.CharField(max_length=100)
    type_stock = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)

    def __str__(self):
        return f"ID: {self.id}, Ticker: {self.ticker}, Nom: {self.name_stock}, Type: {self.type_stock}, Devise: {self.currency}"

class Holding(models.Model):
    id = models.AutoField(primary_key=True)
    sock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    wallet_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Quantité: {self.quantity}, Portefeuille: {self.wallet_id}, Stock: {self.sock_id}"

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

    def __str__(self):
        return f"ID: {self.id}, Quantité: {self.quantity}, Stock: {self.stock_id}, Prix: {self.price}, Conversion: {self.conversion_rate}, Prix EUR: {self.price_eur}, Montant total: {self.total_amount}, Charges: {self.charges}, Portefeuille: {self.wallet_id}, Date: {self.date}"

class WalletCashflow(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    cashflow_entry = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(Holder, on_delete=models.CASCADE)
    wallet_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Date: {self.date}, Entrée de trésorerie: {self.cashflow_entry}, Utilisateur: {self.user_id}, Portefeuille: {self.wallet_id}"
