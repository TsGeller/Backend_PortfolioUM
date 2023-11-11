

from rest_framework import generics

from dashboard.models import Holder, Holding, Portfolio, Stock,ActorCashflow, WalletCashflow
from dashboard.serializers import HoldingSerializer, StockSerializer,ActorCashflowSerializer,PortfolioSerializer,HolderSerializer, WalletCashflowSerializer


class StockListAPI(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
class ActorCashflowListApi(generics.ListAPIView):
    queryset = ActorCashflow.objects.all()
    serializer_class = ActorCashflowSerializer
class HoldingListApi(generics.ListAPIView):
    queryset = Holding.objects.all()
    serializer_class = PortfolioSerializer
class PortfolioListApi(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
class HolderListApi(generics.ListAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
class WalletCashflowListApi(generics.ListAPIView):
    queryset = WalletCashflow.objects.all()
    serializer_class = WalletCashflowSerializer
