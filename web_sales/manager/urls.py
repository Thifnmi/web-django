from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index-admin"),
    path('mailbox',views.mailbox,name="mailbox-admin"),
    path('mailbox/<str:id>',views.mailbox_detail,name="maildetail-admin"),
    path('login/',views.login,name="login-admin"),
    path('logout/',views.login,name="logout-admin"),
    path('users/',views.user,name="users"),
    path('users/add/',views.adduser,name="add-user"),
    path('users/edit/',views.edituser,name="edit-user"),
    path('users/profile',views.userdetail,name="profile-user"),
    path('products/',views.products,name="manager-product"),
    path('products/add/',views.addproduct,name="add-product"),
    path('products/edit/',views.editproduct,name="edit-product"),
    path('products/detail/',views.productdetail,name="product-detail"),
    path('categories/',views.categories,name="manager-category"),
    path('categories/add/',views.addcategories,name="add-category"),
    path('categories/edit/',views.editcategories,name="edit-category"),
    # path('categories/detail/',views.categorydetail,name="category-detail"),
    path('invoices/',views.invoices,name="manager-invoice"),
    path('invoices/add/',views.addinvoice,name="add-invoice"),
    path('invoices/edit/',views.editinvoice,name="edit-invoice"),
    path('invoices/detail/',views.invoicedetial,name="invoice-detail"),
    path('suppliers/',views.supplier,name="manager-supplier"),
    path('suppliers/add/',views.addsupplier,name="add-supplier"),
    path('suppliers/edit/',views.editsupplier,name="edit-supplier"),
    path('suppliers/detail/',views.supplierdetail,name="supplier-detail"),
    
]
