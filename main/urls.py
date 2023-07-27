from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop/product_details', views.product_details, name='product_details'),
    path('shop/cart', views.shop_cart, name='shop_cart'),
    path('shop/checkout', views.shop_checkout, name='shop_checkout'),
    path('contact', views.contact, name='contact'),
    path('login', views.client_login, name='client_login'),
    path('register', views.client_register, name='client_register'),
]
