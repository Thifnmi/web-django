from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:id>",views.shop, name="category"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
    path("account/cart/",views.cart, name="cart"),
    path("contact/",views.contact, name="contact"),
    path("account/checkout/",views.checkout, name="checkout"),
    path("product-detail/<str:id>",views.product_detail, name="detail"),
    path("register/",views.register, name="register"),
    path("account/profile/",views.profile, name="profile"),
    path("supplier/<str:id>",views.supplier, name="supplier"),
]
