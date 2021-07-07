# from django.db import models
from djongo import models

# Create your models here.
class About(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    image = models.TextField()
    content1 = models.TextField()
    content2 = models.TextField()
class banner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    link = models.TextField()

class category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    metaTitle = models.TextField()
    description = models.TextField()

class contact(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    content = models.TextField()

class image(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    imageThumb = models.TextField()
    imageSmall = models.TextField()
    content = models.TextField()

class orders(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    fullname = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    note = models.TextField()
    create_on = models.TextField()
    shipping_status = models.TextField()
    bill_address = models.TextField()

class order_detail(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    total_price = models.IntegerField()
    product_amount = models.IntegerField()

class product(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    supplier_id = models.IntegerField()
    name = models.TextField()
    quantity = models.TextField()
    link = models.TextField()
    image = models.TextField()
    price = models.TextField()
    productCode = models.TextField()
    featureData = models.TextField()

class supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.TextField()
    image = models.TextField()
    weburl = models.TextField()
    telephone = models.TextField()
    email = models.TextField()
    country = models.TextField()
    address = models.TextField()

class users(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.TextField()
    username = models.TextField()
    password = models.TextField()
    fullname = models.TextField()
    birthday = models.TextField()
    gender = models.TextField()
    phonenumber = models.TextField()
    email = models.TextField()
    address = models.TextField()
    country = models.TextField()
    role_id = models.IntegerField()
    facebook = models.TextField()
    twitter = models.TextField()
    gmail = models.TextField()
    instagram = models.TextField()