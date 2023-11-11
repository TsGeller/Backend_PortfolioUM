from rest_framework import generics

from dashboard.models import ActorCashflow, Holder, Holding, Portfolio, Stock, WalletCashflow
from dashboard.serializers import ActorCashflowSerializer, HolderSerializer, HoldingSerializer, PortfolioSerializer, StockSerializer, WalletCashflowSerializer

class HolderDeleteApi(generics.DestroyAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
class StockDeleteApi(generics.DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class PortfolioDeleteApi(generics.DestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
class HoldingDeleteApi(generics.DestroyAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer
class ActorCashflowDeleteApi(generics.DestroyAPIView):
    queryset = ActorCashflow.objects.all()
    serializer_class = ActorCashflowSerializer
class WalletCashflowDeleteApi(generics.DestroyAPIView):
    queryset = WalletCashflow.objects.all()
    serializer_class = WalletCashflowSerializer
