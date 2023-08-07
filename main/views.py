from django.shortcuts import render

from main.models import *


# Create your views here.
def handle_not_found(request, exception):
    return render(request, 'main/404.html')



def home(request):
    categories = ProductCategory.objects.filter()
    context = {
        'categories': categories,
    }
    return render(request, 'main/home.html', context);



def about(request):
    return render(request, 'main/about.html');



def contact(request):
    return render(request, 'main/contact.html');



def shop(request):
    categories = ProductCategory.objects.filter()
    products = Product.objects.filter()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'main/shop.html', context);



def product_details(request):
    return render(request, 'main/product_details.html');



def shop_cart(request):
    return render(request, 'main/cart.html');



def shop_checkout(request):
    return render(request, 'main/checkout.html');



def order_confirmation(request):
    return render(request, 'main/confirmation.html');



def order_tracking(request):
    return render(request, 'main/tracking.html');



def client_login(request):
    return render(request, 'main/login.html');



def client_register(request):
    return render(request, 'main/register.html');