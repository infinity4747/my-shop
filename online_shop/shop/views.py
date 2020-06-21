from django.shortcuts import render
import requests
# Create your views here.
def index(request):
	r = requests.get('http://127.0.0.1:8000/product/3')
	print(r.status)
	return render(request,"index.html",{'product':r.content})
def shop(request):
	return render(request,"shop.html")
def login(request):
	return render(request,"login-register.html")
def product(request):
	return render(request,"product-details.html")
def cart(request):
	return render(request,"cart.html")