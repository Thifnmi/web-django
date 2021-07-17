from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index-admin"),
    path('mailbox',views.mailbox,name="mailbox-admin"),
    path('mailbox/<str:id>',views.mailbox_detail,name="maildetail-admin"),
    path('login/',views.login,name="login-admin"),
    path('logout/',views.logout,name="logout-admin"),
    path('users/',views.user,name="users"),
    path('users/add/',views.adduser,name="add-user"),
    path('users/edit/<str:id>',views.edituser,name="edit-user"),
    path('users/profile/<str:id>',views.userdetail,name="profile-user"),
    path('products/',views.products,name="manager-product"),
    path('products/add/',views.addproduct,name="add-product"),
    path('products/edit/<str:id>',views.editproduct,name="edit-product"),
    path('products/detail/<str:id>',views.productdetail,name="product-detail"),
    path('categories/',views.categories,name="manager-category"),
    path('categories/add/',views.addcategories,name="add-category"),
    path('categories/edit/<str:id>',views.editcategories,name="edit-category"),
    path('invoices/',views.invoices,name="manager-invoice"),
    path('invoices/add/',views.addinvoice,name="add-invoice"),
    path('invoices/edit/<str:id>',views.editinvoice,name="edit-invoice"),
    path('invoices/detail/<str:id>',views.invoicedetial,name="invoice-detail"),
    path('suppliers/',views.supplier,name="manager-supplier"),
    path('suppliers/add/',views.addsupplier,name="add-supplier"),
    path('suppliers/edit/<str:id>',views.editsupplier,name="edit-supplier"),
    path('suppliers/detail/<str:id>',views.supplierdetail,name="supplier-detail"),   
]
