from django.urls import path
from .views import PaymentView, GatewayView


urlpatterns = [
    # payments
    path('pay/', PaymentView.as_view(), name='payments'),
    # gateways
    path('gateways/', GatewayView.as_view(), name='gateways'),
]