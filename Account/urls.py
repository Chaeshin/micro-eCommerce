from django.urls import path
from . import views
from .views import logout_view

app_name = 'Account'
urlpatterns = [
    path('',views.index, name='index'), #127.0.0.1/account
    # path('register/', views.register, name='register'),

    path('Register/', views.CustomerRegistrations.as_view(), name='Register'),
    path('Login/', views.CustomerLogins.as_view(), name='Login'),
    path('logout/', logout_view, name='logout'),
]