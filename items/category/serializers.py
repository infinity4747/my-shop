from .models import Category,Product
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("categoryId","name")
class ProductSerializer(serializers.ModelSerializer):
    categoryId=CategorySerializer()
    class Meta:
        model = Product
        fields = ("productId","name", "categoryId","price")
class ProductSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("productId","name", "categoryId","price")