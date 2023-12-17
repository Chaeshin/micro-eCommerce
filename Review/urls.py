from django.urls import path
from . import views
app_name = 'Review'
urlpatterns = [
     #127.0.0.1/account
    # path('register/', views.register, name='register'),

    path('toReviewsPage/', views.toReview.as_view(), name='toReview'),
    path('myReviewsPage/', views.myReview.as_view(), name='myReview'),
    path('ReviewsPage/<int:orderitem_id>/', views.productReview.as_view(), name='Review'),

]