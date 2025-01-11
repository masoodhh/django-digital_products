"""
URL configuration for digital_products project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import ProductListView, ProductDetailsView, CategoryListView, CategoryDetailsView, FileListView, \
    FileDetailsView

urlpatterns = [
    # products
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailsView.as_view(), name='product-detail'),
    # files
    path('products/<int:product_id>/files/', FileListView.as_view(), name='files'),
    path('products/<int:product_id>/files/<int:pk>', FileDetailsView.as_view(), name='file-detail'),
    # categories
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetailsView.as_view(), name='category-detail'),
]
