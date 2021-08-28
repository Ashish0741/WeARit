from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="images",default="")

    def getproductsbyid(ids):
        return Product.objects.filter(id__in = ids)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    
    def __str__(self):
        return self.user

class Contact(models.Model):
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.user