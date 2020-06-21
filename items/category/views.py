from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer,ProductSerializer,ProductSerializerPost
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Category,Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView,CreateAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class GetView(ListAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def update(self, request,pk, *args, **kwargs):
        try:

            snippet = Category.objects.get(pk=pk)
            serializer = CategorySerializer(snippet,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status":"successful"})
        except:
        	return JsonResponse({'status': 'error'})
    def get(self, request, pk):
        try:
        	category = Category.objects.filter(categoryId=pk,status=1)
        	serializer = CategorySerializer(category, many=True)
        	return JsonResponse({"status":"successful","category": serializer.data})
        except:
        	return JsonResponse({"status":"error"})

    def delete(self,request,pk):
        try:
            category = Category.objects.get(categoryId=pk)
            category.status=0
            category.save()
            
            serializer = CategorySerializer(category, many=True)
            return JsonResponse({"status":"successful"})
        except:
            return JsonResponse({"status": "error"})
class PostView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return JsonResponse({'status': 'You have successfully register'})
        except:
        	return JsonResponse({'status': 'error'})
class GetAllView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name')
    def get(self, request):
        try:
        	category = Category.objects.all()[:6]
        	serializer = CategorySerializer(category, many=True)
        	return JsonResponse({"status":"successful","Category": serializer.data})
        except:
        	return JsonResponse({"status":"error"})

class GetProductView(ListAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerPost
    
    def get(self, request, pk):
        try:
        	product = Product.objects.filter(productId=pk,status=1)
        	serializer = ProductSerializer(product, many=True)
        	return JsonResponse({"status":"successful","product": serializer.data})
        except:
        	return JsonResponse({"status":"error"})

    def delete(self,request,pk):
        try:
            product = Product.objects.get(productId=pk)
            product.status=0
            product.save()
            
            serializer = ProductSerializer(product, many=True)
            return JsonResponse({"status":"successful"})
        except:
            return JsonResponse({"status": "error"})
class PostProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerPost
    def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return JsonResponse({'status': 'You have successfully create'})

class GetAllProductView(ListAPIView):
    queryset = Product.objects.all()[:10]
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name')
    def get(self, request):
        try:
        	category = Product.objects.all()[:10]
        	serializer = ProductSerializer(category, many=True)
        	return JsonResponse({"status":"successful","Product": serializer.data})
        except:
        	return JsonResponse({"status":"error"})