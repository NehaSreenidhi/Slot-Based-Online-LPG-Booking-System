from django.urls import path 
from . import views

#root - url pattern , views - function (from views.py), name - identifies.

urlpatterns = [
    path('', views.home, name='home'),  
    path('book/', views.book, name='book'),
    path('cancel/', views.cancel, name='cancel'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('manage_orders/', views.manage_orders, name='manage_orders'),
    path('customer_orders/', views.customer_orders, name='customer_orders'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<int:user_id>/', views.reset_password, name='reset_password'),
]