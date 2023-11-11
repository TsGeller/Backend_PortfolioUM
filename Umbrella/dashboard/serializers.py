from rest_framework import serializers
from .models import Holder, Holding, Stock,Portfolio, WalletCashflow
from .models import ActorCashflow

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class ActorCashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorCashflow
        fields = '__all__'

class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holding
        fields = '__all__'
        
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = '__all__'
class WalletCashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletCashflow
        fields = '__all__'
