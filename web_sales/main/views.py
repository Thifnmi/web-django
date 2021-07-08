from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage
from django.views.decorators.csrf import csrf_exempt
from .models import banner,product,users,supplier,orders,order_detail,category,contact,About,image


# Create your views here.
@csrf_exempt
def index(respone):
    categories = category.objects.all()
    return render(respone, "client/index.html", {"categories" : categories})

def shop(respone, id):
    sp_list = product.objects.filter(category_id = str(id))
    title = category.objects.get(id=str(id))
    categories = category.objects.all()
    paginator  = Paginator(sp_list, 8)

    page_number = respone.GET.get('page')
    sp = paginator.get_page(page_number)
    return render(respone, "client/category.html", {"sp": sp, "title" : title, "categories" : categories})
    
def login(respone):
    categories = category.objects.all()
    return render(respone, "client/login.html",{"categories" : categories})

def product_detail(respone, id):
    detail = product.objects.get(id=str(id))
    # print(detail.id)
    categories = category.objects.all()
    product_image = image.objects.filter(product_id = str(detail.id))
    # print(product_image)
    return render(respone, "client/product-details.html", {"detail": detail,"product_image" : product_image, "categories" : categories})

def contact(respone):
    categories = category.objects.all()
    return render(respone, "client/contact-us.html",{"categories" : categories})

def checkout(respone):
    categories = category.objects.all()
    return render(respone, "client/checkout.html",{"categories" : categories})

def cart(respone):
    categories = category.objects.all()
    return render(respone, "client/cart.html",{"categories" : categories})

def register(respone):
    categories = category.objects.all()
    return render(respone, "client/register.html",{"categories" : categories})

def profile(respone):
    categories = category.objects.all()
    return render(respone, "client/profile.html",{"categories" : categories})