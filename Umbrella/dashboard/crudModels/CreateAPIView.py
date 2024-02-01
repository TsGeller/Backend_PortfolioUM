import genericpath

from rest_framework import generics

from dashboard.models import Holder, Holding, Portfolio, Stock,ActorCashflow, WalletCashflow
from dashboard.serializers import ActorCashflowSerializer, HolderSerializer, HoldingSerializer, PortfolioSerializer, StockSerializer, WalletCashflowSerializer

## create stock api
class StockCreateApi(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class HolderCreateApi(generics.CreateAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
class PortfolioCreateApi(generics.CreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
class HoldingCreateApi(generics.CreateAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer
class ActorCashflowCreateApi(generics.CreateAPIView):
    queryset = ActorCashflow.objects.all()
    serializer_class = ActorCashflowSerializer
class WalletCashflowCreateApi(generics.CreateAPIView):
    queryset = WalletCashflow.objects.all()
    serializer_class = WalletCashflowSerializer
