from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import banner,product,users,supplier,orders,order_detail,category,contact,About,image

# Create your views here.
@csrf_exempt
def index(response):
    return render(response, "page/index.html")

def login(response):
    return render(response, "page/login.html")

def logout(response):
    return render(response, "page/login.html")

def user(response):
    return render(response, "page/users/all-user.html")

def adduser(response):
    return render(response, "page/users/add-user.html")

def edituser(response):
    return render(response, "page/users/edit-user.html")

def userdetail(response):
    return render(response, "page/users/profile.html")

def categories(response):
    return render(response, "page/categories/all-category.html")

def addcategories(response):
    return render(response, "page/categories/add-category.html")

def editcategories(response):
    return render(response, "page/categories/edit-category.html")

def categorydetail(response):
    return render(response, "page/categories/category-detail.html")

def invoices(response):
    return render(response, "page/invoices/all-invoice.html")

def addinvoice(response):
    return render(response, "page/invoices/add-invoice.html")

def editinvoice(response):
    return render(response, "page/invoices/edit-invoice.html")

def invoicedetial(response):
    return render(response, "page/invoices/invoice-detail.html")

def products(response):
    return render(response, "page/products/all-product.html")

def addproduct(response):
    return render(response, "page/products/add-product.html")

def editproduct(response):
    return render(response, "page/products/edit-product.html")

def productdetail(response):
    return render(response, "page/products/product-detail.html")

def supplier(response):
    return render(response, "page/suppliers/all-supplier.html")

def addsupplier(response):
    return render(response, "page/suppliers/add-supplier.html")

def editsupplier(response):
    return render(response, "page/suppliers/edit-supplier.html")

def supplierdetail(response):
    return render(response, "page/suppliers/supplier-detail.html")

