from django.db import models
from Account.models import Customer
from Product.models import Product


class ReviewVote(models.Model):
    review_vote_id = models.BigAutoField(primary_key=True)
    choices = [
        ("NO", "No action"),
        ("LK", "Liked"),
        ("DK", "Disliked"),
    ]
    vote_type = models.CharField(max_length=2, choices=choices, default="NO")


class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_vote = models.ForeignKey(ReviewVote, models.SET_NULL, null=True)
    comment = models.CharField(max_length=100)
