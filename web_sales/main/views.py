from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage
from django.views.decorators.csrf import csrf_exempt
from .models import banner,product,users,supplier,orders,order_detail,category,contact,About,image


# Create your views here.
@csrf_exempt
def index(respone):
    suppliers = supplier.objects.all()
    categories = category.objects.all()
    ao = product.objects.filter(category_id=1).order_by()[:4]
    quandai = product.objects.filter(category_id=2).order_by()[:4]
    vaydam = product.objects.filter(category_id=3).order_by()[:4]
    tuixach = product.objects.filter(category_id=4).order_by()[:4]
    giay = product.objects.filter(category_id=5).order_by()[:4]
    vi = product.objects.filter(category_id=6).order_by()[:4]
    kinh = product.objects.filter(category_id=7).order_by()[:4]
    vo = product.objects.filter(category_id=8).order_by()[:4]
    return render(respone, "client/index.html", {"suppliers": suppliers,"categories" : categories,
    "ao":ao,"quaidai":quandai, "vaydam":vaydam,"tuixach":tuixach,"giay":giay,"vi":vi,"kinh":kinh,"vo":vo})

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