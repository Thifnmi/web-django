from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/",views.shop, name="shop"),
    path("login/",views.login, name="login"),
    path("account/cart/",views.cart, name="cart"),
    path("contact/",views.contact, name="contact"),
    path("account/checkout/",views.checkout, name="checkout"),
    path("product-detail/",views.product_detail, name="product-detail"),
    path("register/",views.register, name="register"),
    path("account/profile/",views.profile, name="profile"),
]
