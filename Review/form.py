import Product as Product
from django.forms import ModelForm
from django import forms
from .models import Review


class CustomerReview(ModelForm):

    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comment'}))

    class Meta:
        model = Review
        fields = ['comment', 'customer', 'review_vote']

    # Product = forms.ModelChoiceField(
    #     queryset=Product.objects.all(),
    #     widget=forms.Select(attrs={'class': 'custom-select'}),
    # )