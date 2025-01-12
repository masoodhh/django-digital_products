from django.urls import path
from .views import SubscriptionView,  PackageView

urlpatterns = [
    # subscriptions
    path('subscriptions/', SubscriptionView.as_view(), name='subscriptions'),
    # packages
    path('packages/', PackageView.as_view(), name='packages'),
]