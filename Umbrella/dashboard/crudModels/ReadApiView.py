

from rest_framework import generics

from dashboard.models import Holder, Holding, Portfolio, Stock,ActorCashflow, WalletCashflow
from dashboard.serializers import HoldingSerializer, StockSerializer,ActorCashflowSerializer,PortfolioSerializer,HolderSerializer, WalletCashflowSerializer


class StockReadApiView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class ActorCashflowReadApiView(generics.ListAPIView):
    queryset = ActorCashflow.objects.all()
    serializer_class = ActorCashflowSerializer
class HoldingReadApiView(generics.ListAPIView):
    queryset = Holding.objects.all()
    serializer_class = PortfolioSerializer
class PortfolioReadApiView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
class HolderReadApiView(generics.ListAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
class WalletCashflowReadApiView(generics.ListAPIView):
    queryset = WalletCashflow.objects.all()
    serializer_class = WalletCashflowSerializer
