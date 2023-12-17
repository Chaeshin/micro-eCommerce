from django.db import models
from Account.models import Customer
from Order.models import OrderItem


class ReviewVote(models.Model):
    review_vote_id = models.BigAutoField(primary_key=True)
    choices = [
        ("NO", "No action"),
        ("LK", "Liked"),
        ("DK", "Disliked"),
    ]
    vote_type = models.CharField(max_length=2, choices=choices, default="NO")

    def __str__(self):
        return str(self.review_vote_id)

class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderitem_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
    review_vote = models.ForeignKey(ReviewVote, models.SET_NULL, null=True)
    comment = models.CharField(max_length=255, default="")
    rate = models.IntegerField(default=0)
    date = models.DateField(auto_now=True, editable=False)
    time = models.TimeField(auto_now=True, editable=False)
    def __str__(self):
        return str(self.review_id)