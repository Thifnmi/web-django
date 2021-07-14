from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.sessions.backends.base import SessionBase
from main.models import banner,product,users,orders,order_detail,category,contact,About,image,provider

# Create your views here.

def index(response):
    if not response.session._session:
        return redirect("login-admin")
    return render(response, "page/dashboard.html", {})

@csrf_exempt
def mailbox(response):
    if not response.session._session:
        return redirect("login-admin")
    return render(response, "page/mailbox.html")

@csrf_exempt
def mailbox_detail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    return render(response, "page/mail_detail.html")

@csrf_exempt
def login(response):
    if(response.method == 'POST'):
        username = response.POST.get('username','')
        password = response.POST.get('password','')
        account = users.objects.get(username=username)
        if (account.password == password and account.role_id != "2"):
            response.session['id'] = account.id
            response.session.set_expiry(120)
            response.session.modified = True
            return redirect("index-admin")
        else:
            messages.error(response,"Username or password don\'t match")
            return render(response,"page/login.html")
        
    return render(response, "page/login.html")

@csrf_exempt
def logout(response):
    if not response.session._session:
        return redirect("login-admin")
    del response.session['id']
    return logout(response)

@csrf_exempt
def user(response):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.all()
    return render(response, "page/account/index.html",{"user":user})

@csrf_exempt
def adduser(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("users")
    return render(response, "page/account/add.html")

@csrf_exempt
def edituser(response,id):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("user")
    userdetail = users.objects.get(id=id)
    return render(response, "page/account/edit.html",{"userdetail":userdetail})

@csrf_exempt
def userdetail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    userdetail = users.objects.get(id=id)
    return render(response, "page/account/profile.html",{"userdetail":userdetail})

@csrf_exempt
def categories(response):
    if not response.session._session:
        return redirect("login-admin")
    categories = category.objects.all()
    return render(response, "page/category/index.html",{"categories":categories})

@csrf_exempt
def addcategories(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-category")
    return render(response, "page/category/add.html")

@csrf_exempt
def editcategories(response,id):
    if not response.session._session:
        return redirect("login-admin")
    categorydetail = category.objects.get(id=id)
    
    if(response.method =='POST'):
        return redirect("manager-category")
    return render(response, "page/category/edit.html",{"categorydetail":categorydetail})

@csrf_exempt
def invoices(response):
    if not response.session._session:
        return redirect("login-admin")
    return render(response, "page/invoice/index.html")

@csrf_exempt
def addinvoice(response):
    if not response.session._session:
        return redirect("login-admin")
    
    if(response.method =='POST'):
        return redirect("manager-invoice")
    return render(response, "page/invoice/add.html")

@csrf_exempt
def editinvoice(response,id):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-invoice")
    return render(response, "page/invoice/edit.html")

@csrf_exempt
def invoicedetial(response,id):
    if not response.session._session:
        return redirect("login-admin")
    return render(response, "page/invoice/detail.html")

@csrf_exempt
def products(response):
    if not response.session._session:
        return redirect("login-admin")
    products = product.objects.all()
    suppliers = provider.objects.all()
    return render(response, "page/product/index.html",{"products":products,"suppliers":suppliers})

@csrf_exempt
def addproduct(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-product")
    return render(response, "page/product/add.html")

@csrf_exempt
def editproduct(response,id):
    if not response.session._session:
        return redirect("login-admin")
    products = product.objects.all()
    productdetail = product.objects.get(id=id)
    categories = category.objects.all()
    suppliers = provider.objects.all()
    if(response.method =='POST'):
        return redirect("manager-product")
    return render(response, "page/product/edit.html",{"productdetail":productdetail,"categories": categories,"suppliers":suppliers})

@csrf_exempt
def productdetail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    productdetail = product.objects.get(id=id)
    images = image.objects.filter(product_id = id)
    return render(response, "page/product/detail.html",{"productdetail":productdetail, "images": images})

@csrf_exempt
def supplier(response):
    if not response.session._session:
        return redirect("login-admin")
    supplier = provider.objects.all()
    return render(response, "page/supplier/index.html",{"supplier":supplier})

@csrf_exempt
def addsupplier(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-supplier")
    return render(response, "page/supplier/add.html")

@csrf_exempt
def editsupplier(response,id):
    if not response.session._session:
        return redirect("login-admin")
    supplier = provider.objects.get(id=id)
    if(response.method =='POST'):
        return redirect("manager-supplier")
    return render(response, "page/supplier/edit.html",{"supplier":supplier})

@csrf_exempt
def supplierdetail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    supplier = provider.objects.get(id=id)
    return render(response, "page/supplier/detail.html",{"supplier":supplier})

