from rest_framework import serializers
from .models import Product, Category, File


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ['id','file', 'title','file_type']
    def get_file_type(self, obj):
        return obj.get_file_type_display()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title', 'description', 'avatar']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'avatar', 'categories', 'files', 'url']
