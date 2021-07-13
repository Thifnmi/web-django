from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from main.models import banner,product,users,orders,order_detail,category,contact,About,image,provider

# Create your views here.
@csrf_exempt
def index(response):
    suppliers = provider.objects.all()
    return render(response, "page/dashboard.html", {"suppliers":suppliers})

def mailbox(response):
    return render(response, "page/mailbox.html")

def mailbox_detail(response,id):
    return render(response, "page/mail_detail.html")

def login(response):
    return render(response, "page/login.html")

def logout(response):
    return render(response, "page/login.html")

def user(response):
    user = users.objects.all()
    return render(response, "page/account/index.html",{"user":user})

def adduser(response):
    if(response.method =='POST'):
        return redirect("users")
    return render(response, "page/account/add.html")

def edituser(response,id):
    if(response.method =='POST'):
        return redirect("user")
    userdetail = users.objects.get(id=id)
    return render(response, "page/account/edit.html",{"userdetail":userdetail})

def userdetail(response,id):
    userdetail = users.objects.get(id=id)
    return render(response, "page/account/profile.html",{"userdetail":userdetail})

def categories(response):
    categories = category.objects.all()
    return render(response, "page/category/index.html",{"categories":categories})

def addcategories(response):
    if(response.method =='POST'):
        return redirect("manager-category")
    return render(response, "page/category/add.html")

def editcategories(response,id):
    categorydetail = category.objects.get(id=id)
    
    if(response.method =='POST'):
        return redirect("manager-category")
    return render(response, "page/category/edit.html",{"categorydetail":categorydetail})

def invoices(response):
    return render(response, "page/invoice/index.html")

def addinvoice(response):
    
    if(response.method =='POST'):
        return redirect("manager-invoice")
    return render(response, "page/invoice/add.html")

def editinvoice(response,id):
    if(response.method =='POST'):
        return redirect("manager-invoice")
    return render(response, "page/invoice/edit.html")

def invoicedetial(response,id):
    return render(response, "page/invoice/detail.html")

def products(response):
    products = product.objects.all()
    suppliers = provider.objects.all()
    return render(response, "page/product/index.html",{"products":products,"suppliers":suppliers})

def addproduct(response):
    if(response.method =='POST'):
        return redirect("manager-product")
    return render(response, "page/product/add.html")

def editproduct(response,id):
    products = product.objects.all()
    productdetail = product.objects.get(id=id)
    categories = category.objects.all()
    suppliers = provider.objects.all()
    if(response.method =='POST'):
        return redirect("manager-product")
    return render(response, "page/product/edit.html",{"productdetail":productdetail,"categories": categories,"suppliers":suppliers})

def productdetail(response,id):
    productdetail = product.objects.get(id=id)
    images = image.objects.filter(product_id = id)
    return render(response, "page/product/detail.html",{"productdetail":productdetail, "images": images})

def supplier(response):
    supplier = provider.objects.all()
    return render(response, "page/supplier/index.html",{"supplier":supplier})

def addsupplier(response):
    if(response.method =='POST'):
        return redirect("manager-supplier")
    return render(response, "page/supplier/add.html")

def editsupplier(response,id):
    supplier = provider.objects.get(id=id)
    if(response.method =='POST'):
        return redirect("manager-supplier")
    return render(response, "page/supplier/edit.html",{"supplier":supplier})

def supplierdetail(response,id):
    supplier = provider.objects.get(id=id)
    return render(response, "page/supplier/detail.html",{"supplier":supplier})

