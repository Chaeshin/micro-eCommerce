from django.db import models
from Account.models import Supplier, Customer


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Category, models.SET_NULL, null=True)
    user_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='static/', blank=True, null=True)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

class Wishlist(models.Model):
    wishlist_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
