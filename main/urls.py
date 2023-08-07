from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('shop/product_details/', views.product_details, name='product_details'),
    path('shop/cart/', views.shop_cart, name='shop_cart'),
    path('shop/checkout/', views.shop_checkout, name='shop_checkout'),
    path('shop/order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('shop/order_tracking/', views.order_tracking, name='order_tracking'),
    path('login/', views.client_login, name='client_login'),
    path('register/', views.client_register, name='client_register'),
]
