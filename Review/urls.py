from django.conf.urls.static import static
from django.urls import path

from eCommerce import settings
from . import views
app_name = 'Review'
urlpatterns = [
     #127.0.0.1/account
    # path('register/', views.register, name='register'),

    path('toReviewsPage/', views.toReview.as_view(), name='toReview'),
    path('myReviewsPage/', views.myReview.as_view(), name='myReview'),
    path('ViewProduct/<int:product_id>/', views.ViewProduct.as_view(), name='ViewProduct'),
    path('ReviewsPage/<int:orderitem_id>/', views.productReview.as_view(), name='Review'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)