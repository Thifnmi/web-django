# from django.db import models
from djongo import models

# Create your models here.
class About(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    title = models.TextField()
    image = models.TextField()
    content1 = models.TextField()
    content2 = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_About'

class banner(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    name = models.TextField()
    link = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_banner'

class category(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    name = models.TextField()
    metaTitle = models.TextField()
    description = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_category'

class contact(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    fullname = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    content = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_contact'

class image(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    product_id = models.TextField()
    imageThumb = models.TextField()
    imageSmall = models.TextField()
    content = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_image'

class orders(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    user_id = models.TextField()
    fullname = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    note = models.TextField()
    create_on = models.TextField()
    shipping_status = models.TextField()
    bill_address = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_orders'

class order_detail(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    order_id = models.TextField()
    product_id = models.TextField()
    total_price = models.TextField()
    product_amount = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_order_detail'

class product(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    category_id = models.TextField()
    supplier_id = models.TextField()
    name = models.TextField()
    quantity = models.TextField()
    link = models.TextField()
    image = models.TextField()
    price = models.TextField()
    productCode = models.TextField()
    featureData = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_product'
    

class provider(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
    company_name = models.TextField()
    image = models.TextField()
    weburl = models.TextField()
    telephone = models.TextField()
    email = models.TextField()
    country = models.TextField()
    address = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_provider'

class users(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = models.TextField()
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
    role_id = models.TextField()
    facebook = models.TextField()
    twitter = models.TextField()
    gmail = models.TextField()
    instagram = models.TextField()
    objects = models.DjongoManager()

    class Meta:
        db_table = 'main_users'
