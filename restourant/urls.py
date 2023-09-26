from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login/', views.log_in, name='log'),
    path('register/', views.register, name='register'),
    path("", views.HomeView.as_view(), name='home'),

    path('category/', views.CategoryView.as_view(), name='cate'),
    path('products/', views.ProductView.as_view(), name='product'),

    path('location/', views.LocationView.as_view(), name='location'),
    path("about/", views.AboutView.as_view(), name='about'),

    path('tables/', views.table_view, name='table_list'),
    path('tables/<int:pk>/', views.book_table, name='book_table'),

    path('booking/', booking_view, name='booking_view'),
    # path('room/create/', room_create, name='room_create'),
    path('booking/detail/', booking_detail, name='booking_detail'),
    path('booking/success/', views.booking_success, name='booking_success'),

    path('palov/', views.PalovView.as_view(), name='palov'),
    path('dessert/', views.DessertView.as_view(), name='dessert'),
    path('drinks/', views.DrinksView.as_view(), name='drinks'),
    path('kebab/', views.KebabView.as_view(), name='kebab'),
    path('steak/', views.SteakView.as_view(), name='steak'),
    path('salad/', views.SaladsView.as_view(), name='salad'),

]

