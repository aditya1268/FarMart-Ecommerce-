from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

    
class Store(models.Model):
    store1_name=models.CharField(max_length=100)
    store_username=models.TextField(max_length=10)
    store_password=models.TextField(max_length=10)
    store_address=models.TextField(max_length=500,default="Ravet , Pimpri Chinchwad , Pune , Maharashtra")
    

    def __str__(self)->str:
        return self.store1_name

    class Meta:
        ordering=['store1_name']


class vegetables(models.Model):
    store=models.ForeignKey(Store,related_name="store_veg",on_delete=models.CASCADE)
    # store_username=models.ForeignKey(Store,related_name="store_veg_name",on_delete=models.CASCADE,null=True)
    
    vege_name=models.CharField(max_length=50,null=True)
    vege_descr=models.TextField()
    vege_imag=models.ImageField(upload_to="media")
    vege_count=models.IntegerField()
    vege_price=models.IntegerField()

    category_choices = [
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('flowers', 'Flowers'),
        ('home_products', 'Home Products'),
    ]
    selected_category = models.CharField(max_length=20, choices=category_choices, blank=True, null=True)
    
class User1(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    address = models.TextField()
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)