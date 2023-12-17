from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .form import CustomerRegister, CustomerLogin
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Customer

# Create your views here.


def index(request):
    return HttpResponse("hello world")


class CustomerRegistrations(View):
    template = 'Register.html'

    def get(self,request):
        customer = CustomerRegister()
        return render(request, self.template,{'form': customer})

    def post(self, request):
        form = CustomerRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_type = 'CU'
            user.save()
            login(request, user)
            return redirect('Review:toReview')
        else:
            return render(request, self.template, {'form': form})


class CustomerLogins(View):
    template = 'Login.html'

    def get(self, request):
        customer = CustomerLogin()
        return render(request, self.template, {'form': customer})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('Review:toReview')
        else:
            error_message = "Incorrect username or password!"
            return render(request, self.template, {'form': form, 'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('Account:Login')
