from django.db import models
from Account.models import Courier, Customer
from Payment.models import Payment
from Product.models import Product

class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    courier_id = models.ForeignKey(Courier, models.SET_NULL, null=True)
    payment_id = models.ForeignKey(Payment, models.SET_NULL, null=True)
    choices = [
        ("PR", "Preparing Shipment"),
        ("PE", "Pending"),
        ("DE", "Delivered"),
    ]
    status = models.CharField(max_length=2, choices=choices)

    def __str__(self):
        return str(self.order_id)

class OrderItem(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    status = models.IntegerField(editable=False, default=0)
    def __str__(self):
        return str(self.order_item_id)


