from django.urls import path

from .crudModels.CreateAPIView import ActorCashflowCreateApi, HolderCreateApi, HoldingCreateApi, PortfolioCreateApi, WalletCashflowCreateApi
from .crudModels.DeleteApiView import StockDeleteApi, HolderDeleteApi, PortfolioDeleteApi, HoldingDeleteApi, ActorCashflowDeleteApi, WalletCashflowDeleteApi
from .crudModels.UpdateAPIView import HolderUpdateApi, StockUpdateApi, PortfolioUpdateApi, HoldingUpdateApi, ActorCashflowUpdateApi, WalletCashflowUpdateApi

from .crudModels.ReadApiView import ActorCashflowReadApiView, HolderReadApiView, HoldingReadApiView, PortfolioReadApiView, StockReadApiView, WalletCashflowReadApiView

app_name = 'dashboard'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('stocks/', views.stocks, name='stocks'),
    #path('addstock/', views.addstock, name='addstock'),
    #path('add/', views.add, name='add'),
    #path('addCashflow/', views.addCashflow, name='addCashflow'),
    #path('addTransaction/', views.addTransaction, name='addTransaction'),
    #path('addhold/', views.addhold, name='addhold'),
    #read
    path('api/stocks/', StockReadApiView.as_view(), name='stock-list-api'),
    path('api/actorcashflows/', ActorCashflowReadApiView.as_view(), name='stock-list-api'),
    path('api/holding/', HoldingReadApiView.as_view(), name='stock-list-api'),
    path('api/portfolio/', PortfolioReadApiView.as_view(), name='stock-list-api'),
    path('api/holder/', HolderReadApiView.as_view(), name='stock-list-api'),
    path('api/walletcashflows/', WalletCashflowReadApiView.as_view(), name='stock-list-api'),
    ##Create
    path('api/holder/create/', HolderCreateApi.as_view(), name='holder-create-api'),
    path('api/actorcashflow/create/', ActorCashflowCreateApi.as_view(), name='holder-create-api'),
    path('api/holding/create/', HoldingCreateApi.as_view(), name='holder-create-api'),
    path('api/portfolio/create/', PortfolioCreateApi.as_view(), name='holder-create-api'),
    path('api/WalletCashflow/create/', WalletCashflowCreateApi.as_view(), name='stock-create-api'),
    ##Update
    path('api/holder/<int:pk>/update/', HolderUpdateApi.as_view(), name='holder-update-api'),
    path('api/actorcashflow/<int:pk>/update/', ActorCashflowUpdateApi.as_view(), name='holder-update-api'),
    path('api/holding/<int:pk>/update/', HoldingUpdateApi.as_view(), name='holder-update-api'),
    path('api/portfolio/<int:pk>/update/', PortfolioUpdateApi.as_view(), name='holder-update-api'),
    path('api/stocks/<int:pk>/update/', StockUpdateApi.as_view(), name='stock-update-api'),
    path('api/WalletCashflow/<int:pk>/update/', WalletCashflowCreateApi.as_view(), name='stock-update-api'),
    ##Delete
    path('api/stocks/<int:pk>/delete/', StockDeleteApi.as_view(), name='stock-delete-api'),
    path('api/holder/<int:pk>/delete/', HolderDeleteApi.as_view(), name='holder-delete-api'),
    path('api/holding/<int:pk>/delete/', HoldingDeleteApi.as_view(), name='holder-delete-api'),
    path('api/portfolio/<int:pk>/delete/', PortfolioDeleteApi.as_view(), name='holder-delete-api'),
    path('api/actorcashflow/<int:pk>/delete/', ActorCashflowDeleteApi.as_view(), name='holder-delete-api'),
    path('api/WalletCashflow/<int:pk>/delete/', WalletCashflowCreateApi.as_view(), name='stock-delete-api'),

]
