
from rest_framework import generics
from dashboard.models import ActorCashflow, Holder, Holding, Portfolio, Stock, WalletCashflow
from dashboard.serializers import ActorCashflowSerializer, HolderSerializer, HoldingSerializer, PortfolioSerializer, StockSerializer, WalletCashflowSerializer


class HolderUpdateApi(generics.UpdateAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
class StockUpdateApi(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class PortfolioUpdateApi(generics.UpdateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
class HoldingUpdateApi(generics.UpdateAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer
class ActorCashflowUpdateApi(generics.UpdateAPIView):
    queryset = ActorCashflow.objects.all()
    serializer_class = ActorCashflowSerializer
class WalletCashflowUpdateApi(generics.UpdateAPIView):
    queryset = WalletCashflow.objects.all()
    serializer_class = WalletCashflowSerializer
    