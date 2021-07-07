from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(respone):
    return render(respone, "client/index.html")

def shop(respone):
    return render(respone, "client/shop.html")

def login(respone):
    return render(respone, "client/login.html")

def product_detail(respone):
    return render(respone, "client/product-details.html")

def contact(respone):
    return render(respone, "client/contact-us.html")

def checkout(respone):
    return render(respone, "client/checkout.html")

def cart(respone):
    return render(respone, "client/cart.html")

def register(respone):
    return render(respone, "client/register.html")

def profile(respone):
    return render(respone, "client/profile.html")