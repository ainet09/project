from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login/', views.log_in, name='log'),
    path('register/', views.register, name='register'),

    path("", views.HomeView.as_view(), name='home'),
    path('tables/', views.table_view, name='table_list'),
    path('products/', views.ProductView.as_view(), name='products_list'),

    path('location/', views.LocationView.as_view(), name='location'),
    path("about/", views.AboutView.as_view(), name='about'),

    path('tables/<int:pk>/', views.book_table, name='book_table'),
    path('booking/success/', views.booking_success, name='booking_success'),

    path('booking/', booking_view, name='booking_view'),
    # path('room/create/', room_create, name='room_create'),
    path('booking/detail/', booking_detail, name='booking_detail'),
]

