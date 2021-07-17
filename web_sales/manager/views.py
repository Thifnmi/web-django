from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from main.models import banner,product,users,orders,order_detail,category,contact,About,image,provider
from django.core.files.storage import FileSystemStorage
import string,random

# Create your views here.
def randomname(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    name = ''.join(random.choice(chars) for _ in range(size))
    return name + '.png'
@csrf_exempt
def index(response):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/dashboard.html", {"user":user})

@csrf_exempt
def mailbox(response):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/mailbox.html",{"user":user})

@csrf_exempt
def mailbox_detail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/mail_detail.html",{"user":user})

@csrf_exempt
def login(response):
    if(response.method == 'POST'):
        username = response.POST.get('username')
        password = response.POST.get('password')
        account = users.objects.get(username=username)
        if (account.password == password and account.role_id != "2"):
            response.session['id'] = account.id
            response.session.set_expiry(3600)
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
    return redirect("login-admin")

@csrf_exempt
def user(response):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])

    alluser = users.objects.all()
    return render(response, "page/account/index.html",{"alluser":alluser,"user":user})

@csrf_exempt
def adduser(response):
    if not response.session._session:
        return redirect("login-admin")

    if(response.method =='POST'):
        id = users.objects.all().count() + 1
        alluser = users.objects.all()
        for user in alluser:
            if id == int(user.id):
                id = int(user.id) + 1
            else:
                id = id
        username = response.POST.get('username')
        password = response.POST.get('password')
        fullname = response.POST.get('fullname')
        birthday = response.POST.get('birthday')
        gender = response.POST.get('gender')
        type = response.POST.get('type')
        email = response.POST.get('email')
        phone = response.POST.get('phone')
        address = response.POST.get('address')
        country = response.POST.get('country')
        facebook = response.POST.get('facebook')
        image = response.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        new_account = users(id=id,username=username,password=password, fullname=fullname,birthday=birthday,gender=gender,role_id=type,email=email,phonenumber=phone,address=address,country=country,facebook=facebook,image=uploaded_file_url)
        new_account.save()
        return redirect("users")

    user = users.objects.get(id=response.session['id'])
    return render(response, "page/account/add.html",{"user":user})

@csrf_exempt
def edituser(response,id):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    userdetail = users.objects.get(id=id)
    if(response.method =='POST'):
        userdetail.username = response.POST.get('username')
        userdetail.password = response.POST.get('password')
        userdetail.fullname = response.POST.get('fullname')
        userdetail.birthday = response.POST.get('birthday')
        userdetail.gender = response.POST.get('gender')
        userdetail.email = response.POST.get('email')
        userdetail.phone = response.POST.get('phone')
        userdetail.address = response.POST.get('address')
        userdetail.country = response.POST.get('country')
        userdetail.facebook = response.POST.get('facebook')
        image = response.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        userdetail.image = fs.url(filename)
        userdetail.save()
        return redirect("users")
    
    return render(response, "page/account/edit.html",{"userdetail":userdetail,"user":user})

@csrf_exempt
def userdetail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    userdetail = users.objects.get(id=id)
    return render(response, "page/account/profile.html",{"userdetail":userdetail,"user":user})

@csrf_exempt
def categories(response):
    if not response.session._session:
        return redirect("login-admin")
    categories = category.objects.all()
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/category/index.html",{"categories":categories,"user":user})

@csrf_exempt
def addcategories(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-category")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/category/add.html",{"user":user})

@csrf_exempt
def editcategories(response,id):
    if not response.session._session:
        return redirect("login-admin")
    categorydetail = category.objects.get(id=id)
    
    if(response.method =='POST'):
        return redirect("manager-category")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/category/edit.html",{"categorydetail":categorydetail,"user":user})

@csrf_exempt
def invoices(response):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/invoice/index.html",{"user":user})

@csrf_exempt
def addinvoice(response):
    if not response.session._session:
        return redirect("login-admin")
    
    if(response.method =='POST'):
        return redirect("manager-invoice")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/invoice/add.html",{"user":user})

@csrf_exempt
def editinvoice(response,id):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-invoice")
    return render(response, "page/invoice/edit.html",{"user":user})

@csrf_exempt
def invoicedetial(response,id):
    if not response.session._session:
        return redirect("login-admin")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/invoice/detail.html",{"user":user})

@csrf_exempt
def products(response):
    if not response.session._session:
        return redirect("login-admin")
    products = product.objects.all()
    suppliers = provider.objects.all()
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/product/index.html",{"products":products,"suppliers":suppliers,"user":user})

@csrf_exempt
def addproduct(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-product")
    user = users.objects.get(id=response.session['id'])
    categories = category.objects.all()
    supplier = provider.objects.all()
    return render(response, "page/product/add.html",{"user":user,"categories":categories,"supplier":supplier})

@csrf_exempt
def editproduct(response,id):
    if not response.session._session:
        return redirect("login-admin")
    products = product.objects.all()
    productdetail = product.objects.get(id=id)
    categories = category.objects.all()
    suppliers = provider.objects.all()
    user = users.objects.get(id=response.session['id'])
    if(response.method =='POST'):
        return redirect("manager-product")
    return render(response, "page/product/edit.html",{"user":user,"productdetail":productdetail,"categories": categories,"suppliers":suppliers})

@csrf_exempt
def productdetail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    productdetail = product.objects.get(id=id)
    images = image.objects.filter(product_id = id)
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/product/detail.html",{"user":user,"productdetail":productdetail, "images": images})

@csrf_exempt
def supplier(response):
    if not response.session._session:
        return redirect("login-admin")
    supplier = provider.objects.all()
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/supplier/index.html",{"supplier":supplier,"user":user})

@csrf_exempt
def addsupplier(response):
    if not response.session._session:
        return redirect("login-admin")
    if(response.method =='POST'):
        return redirect("manager-supplier")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/supplier/add.html",{"user":user})

@csrf_exempt
def editsupplier(response,id):
    if not response.session._session:
        return redirect("login-admin")
    supplier = provider.objects.get(id=id)
    if(response.method =='POST'):
        return redirect("manager-supplier")
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/supplier/edit.html",{"supplier":supplier,"user":user})

@csrf_exempt
def supplierdetail(response,id):
    if not response.session._session:
        return redirect("login-admin")
    supplier = provider.objects.get(id=id)
    user = users.objects.get(id=response.session['id'])
    return render(response, "page/supplier/detail.html",{"supplier":supplier,"user":user})

