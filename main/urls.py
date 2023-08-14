from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('shop/category/<str:name>/', views.shopCategory, name='shop_category'),
    path('shop/search/', views.search_result, name='search_result'),
    path('shop/search/<str:search_data>/', views.search_result, name='search_result'),
    path('shop/product/<int:pk>/product_details/', views.product_details, name='product_details'),
    # cart urls
    path('shop/cart/', views.shop_cart, name='shop_cart'),
    path('shop/cart/add_to_cart/<int:product_id>/', views.addToCart, name='add_to_cart'),
    path('shop/cart/update_cart/', views.updateCart, name='update_cart'),
    path('shop/cart/remove_from_cart/<int:product_id>/', views.removeFromCart, name='remove_from_cart'),

    path('shop/checkout/', views.shop_checkout, name='shop_checkout'),
    path('shop/order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('shop/order_tracking/', views.order_tracking, name='order_tracking'),
    path('login/', views.client_login, name='client_login'),
    path('register/', views.client_register, name='client_register'),
    path('client_logout/', views.client_logout, name='client_logout'),
    path('client_account/', views.client_dashboard, name='client_account'),
]
