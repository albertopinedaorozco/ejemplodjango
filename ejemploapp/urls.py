from django.urls import path
from .views import saludar,nuevococinero,consultarpedidos

urlpatterns = [
    path('', saludar),
    path('cocinero/nuevo', nuevococinero),
    path('pedido/', consultarpedidos),
]