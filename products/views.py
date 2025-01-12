from telnetlib import AUTHENTICATION

from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


from .models import Category, File
from .serializers import CategorySerializer, FileSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailsView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailsView(APIView):
    def get_object(self, product_id,pk ):
        try:
            files = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, product_id,pk):

        file = self.get_object(product_id,pk)
        serializer = FileSerializer(file, context={'request': request})
        return Response(serializer.data)
