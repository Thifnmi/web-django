from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import banner,product,users,orders,order_detail,category,contact,About,image,provider
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
@csrf_exempt
def index(response):
    suppliers = provider.objects.all()
    categories = category.objects.all()
    ao = product.objects.filter(category_id=1).order_by()[:4]
    quandai = product.objects.filter(category_id=2).order_by()[:4]
    vaydam = product.objects.filter(category_id=3).order_by()[:4]
    tuixach = product.objects.filter(category_id=4).order_by()[:4]
    giay = product.objects.filter(category_id=5).order_by()[:4]
    vi = product.objects.filter(category_id=6).order_by()[:4]
    kinh = product.objects.filter(category_id=7).order_by()[:4]
    vo = product.objects.filter(category_id=8).order_by()[:4]
    return render(response, "client/index.html", {"suppliers": suppliers,"categories" : categories,"ao":ao,
    "quaidai":quandai, "vaydam":vaydam,"tuixach":tuixach,"giay":giay,"vi":vi,"kinh":kinh,"vo":vo})

def shop(response, id):
    sp_list = product.objects.filter(category_id = str(id))
    title = category.objects.get(id=str(id))
    categories = category.objects.all()
    paginator  = Paginator(sp_list, 8)
    page_number = response.GET.get('page')
    sp = paginator.get_page(page_number)
    return render(response, "client/category.html", {"sp": sp, "title" : title, "categories" : categories})
    
def login(response):
    categories = category.objects.all()
    if(response.method == 'POST'):
        username = response.POST.get('username')
        password = response.POST.get('password')
        account = users.objects.get(username=username)
        if (account.password == password):
            response.session['id'] = account.id
            response.session.set_expiry(3600)
            response.session.modified = True
            return redirect("index")
        else:
            messages.error(response,"Username or password don\'t match")
            return render(response,"client/login.html")
        
    return render(response, "client/login.html",{"categories" : categories})

def logout(response):
    if not response.session._session:
        return redirect("login")
    del response.session['id']
    return redirect("login")

def product_detail(response, id):
    detail = product.objects.get(id=str(id))
    categories = category.objects.all()
    product_image = image.objects.filter(product_id = str(detail.id))
    return render(response, "client/product-details.html", {"detail": detail,"product_image" : product_image, "categories" : categories})

def contact(response):
    categories = category.objects.all()
    return render(response, "client/contact-us.html",{"categories" : categories})

def checkout(response):
    if not response.session._session:
        return redirect("login")
    categories = category.objects.all()
    return render(response, "client/checkout.html",{"categories" : categories})

def cart(response):
    if not response.session._session:
        return redirect("login")
    categories = category.objects.all()
    return render(response, "client/cart.html",{"categories" : categories})

def register(response):
    # if(response.method =='POST'):
    #     id = users.objects.all().count() + 1
    #     alluser = users.objects.all()
    #     for user in alluser:
    #         if id == int(user.id):
    #             id = int(user.id) + 1
    #         else:
    #             id = id
    #     username = response.POST.get('username')
    #     password = response.POST.get('password')
    #     fullname = response.POST.get('fullname')
    #     birthday = response.POST.get('birthday')
    #     gender = response.POST.get('gender')
    #     type = response.POST.get('type')
    #     email = response.POST.get('email')
    #     phone = response.POST.get('phone')
    #     address = response.POST.get('address')
    #     country = response.POST.get('country')
    #     facebook = response.POST.get('facebook')
    #     image = response.FILES['file']
    #     fs = FileSystemStorage()
    #     filename = fs.save(image.name, image)
    #     uploaded_file_url = fs.url(filename)
    #     new_account = users(id=id,username=username,password=password, fullname=fullname,birthday=birthday,gender=gender,role_id=type,email=email,phonenumber=phone,address=address,country=country,facebook=facebook,image=uploaded_file_url)
    #     new_account.save()
    #     return redirect("users")
    categories = category.objects.all()
    return render(response, "client/register.html",{"categories" : categories})

def profile(response):
    if not response.session._session:
        return redirect("login")
    categories = category.objects.all()
    return render(response, "client/profile.html",{"categories" : categories})

def supplier(response,id):
    product_list = product.objects.filter(supplier_id = id)
    paginator  = Paginator(product_list, 8)
    page_number = response.GET.get('page')
    products = paginator.get_page(page_number)
    return render(response, "client/supplier.html",{"products":products})
