from django.shortcuts import render,get_list_or_404, get_object_or_404
from .forms import CreateUserForm
from .serializers import UsersSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters

from rest_framework.generics import GenericAPIView,CreateAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
class GetView(ListAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    def get(self, request, pk):
        user = User.objects.filter(userId=pk,status=1)
        serializer = UsersSerializer(user, many=True)
        return Response({"user": serializer.data})
    def delete(self,request,pk):
        user = User.objects.get(userId=pk)
        user.status=0
        user.save()
        serializer = UsersSerializer(user, many=True)
class PostView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)