from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from user.views import GetView,PostView,LoginView,LogoutView

urlpatterns = [
 	path('created/',PostView.as_view(),name="create"),
    path('<int:pk>',GetView.as_view(),name="get"),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
   
]
