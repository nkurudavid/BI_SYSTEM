from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'main/home.html');



def shop(request):
    return render(request, 'main/product.html');



def product_details(request):
    return render(request, 'main/product_details.html');



def shop_cart(request):
    return render(request, 'main/cart.html');



def shop_checkout(request):
    return render(request, 'main/checkout.html');



def contact(request):
    return render(request, 'main/contact.html');



def client_login(request):
    return render(request, 'main/login.html');



def client_register(request):
    return render(request, 'main/register.html');