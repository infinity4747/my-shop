from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from category.views import GetView,PostView,GetAllView,GetProductView,PostProductView,GetAllProductView

urlpatterns = [
 	path('category/create/',PostView.as_view(),name="create"),
    path('categories',GetAllView.as_view(),name="get"),
    path('category/<int:pk>',GetView.as_view(),name="getAll"),
    path('product/<int:pk>',GetProductView.as_view(),name="getAllProduct"),
    path('products',GetAllProductView.as_view(),name="getAllProduct"),
    path('product/create/',PostProductView.as_view(),name="createProduct"),
    
]
