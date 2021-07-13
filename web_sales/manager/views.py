from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import banner,product,users,supplier,orders,order_detail,category,contact,About,image

# Create your views here.
@csrf_exempt
def index(response):
    categories = category.objects.all()
    return render(response, "page/dashboard.html", {"categories": categories})

def mailbox(response):
    return render(response, "page/mailbox.html")

def mailbox_detail(response):
    return render(response, "page/mail_detail.html")

def login(response):
    return render(response, "page/login.html")

def logout(response):
    return render(response, "page/login.html")

def user(response):
    return render(response, "page/account/index.html")

def adduser(response):
    return render(response, "page/account/add.html")

def edituser(response):
    return render(response, "page/account/edit.html")

def userdetail(response):
    return render(response, "page/account/profile.html")

def categories(response):
    return render(response, "page/category/index.html")

def addcategories(response):
    return render(response, "page/category/add.html")

def editcategories(response):
    return render(response, "page/category/edit.html")

# def categorydetail(response):
#     return render(response, "page/category/category-detail.html")

def invoices(response):
    return render(response, "page/invoice/index.html")

def addinvoice(response):
    return render(response, "page/invoice/add.html")

def editinvoice(response):
    return render(response, "page/invoice/edit.html")

def invoicedetial(response):
    return render(response, "page/invoice/detail.html")

def products(response):
    return render(response, "page/product/index.html")

def addproduct(response):
    return render(response, "page/product/add.html")

def editproduct(response):
    return render(response, "page/product/edit.html")

def productdetail(response):
    return render(response, "page/product/detail.html")

def supplier(response):
    return render(response, "page/supplier/index.html")

def addsupplier(response):
    return render(response, "page/supplier/add.html")

def editsupplier(response):
    return render(response, "page/supplier/edit.html")

def supplierdetail(response):
    return render(response, "page/supplier/detail.html")

