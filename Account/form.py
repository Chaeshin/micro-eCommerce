from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Customer


class CustomerRegister(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    mobile_number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Mobile Number', 'type': 'number','step': 'any'}))
    user_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    user_type = forms.CharField(widget=forms.HiddenInput, initial="CU")

    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'mobile_number', 'user_address', 'age', 'user_type']

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if len(username) < 5:
    #         raise ValidationError("Username must be at least 5 characters long.")
    #     # Add more checks for uniqueness and valid characters
    #
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if len(password) < 8:
    #         raise ValidationError("Password must be at least 8 characters long.")
    #     # Add more checks for complexity
    #
    #
    #
    # def clean_mobile_number(self):
    #     mobile_number = self.cleaned_data.get('mobile_number')


class CustomerLogin(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = Customer
        fields = ['username', 'password']



