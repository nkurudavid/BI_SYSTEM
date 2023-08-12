from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

from django.db.models import Q

from main.models import *



# my functions
def search_products_filter(search_data=None):
    if search_data:
        # get data where category name contains search_data or product name contains search_data
        matched_products = ProductDetail.objects.filter(Q(product__category__category_name__icontains=search_data) | Q(product__product_name__icontains=search_data))
    return matched_products



# Create your views here.
def handle_not_found(request, exception):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        context = {
            'title': 'Page Not found',
        }
        return render(request, 'main/404.html', context)



def home(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        categories = ProductCategory.objects.filter()
        context = {
            'title': 'Welcome',
            'categories': categories,
        }
        return render(request, 'main/home.html', context)



def about(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        context = {
            'title': 'About us',
        }
        return render(request, 'main/about.html', context)



def contact(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        context = {
            'title': 'Contact us',
        }
        return render(request, 'main/contact.html', context)



def shop(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        categories = ProductCategory.objects.filter()
        products = ProductDetail.objects.filter()
        context = {
            'title': 'Shop',
            'categories': categories,
            'products': products,
        }
        return render(request, 'main/shop.html', context)



def search_result(request, search_data=None):
    if search_data:
        # Call the search_products_filter function to get the filtered products
        filtered_products = search_products_filter(search_data)

        categoryData = ProductCategory.objects.filter()
        context = {
            'title': 'Shop - Search Result',
            'categories': categoryData,
            'products': filtered_products,
        }
        return render(request, 'main/search_result.html', context)
    else:
        return redirect(shop)



def shopCategory(request, name):
    category_name = name
    # check if category exist
    if ProductCategory.objects.filter(category_name=category_name).exists():
        # if exists
        selectedCategory = ProductCategory.objects.get(category_name=category_name)
        products = ProductDetail.objects.filter(product__category=selectedCategory)

        if 'search' in request.POST:
            search_data = request.POST.get("search_data")

            if search_data:
                # Call the search_result function and pass the data
                return search_result(request, search_data)
            else:
                return redirect(shop)
        else:
            categories = ProductCategory.objects.filter()
            context = {
                'title': 'Shop - category',
                'categories': categories,
                'products': products,
                'selectedCategory': selectedCategory,
            }
            return render(request, 'main/shop.html', context)
    else:
        messages.error(request, ('Product Category not found'))
        return redirect(shop)




def product_details(request, pk):
    product_id = pk
    # check if category exist
    if ProductDetail.objects.filter(id=product_id).exists():
        # if exists
        selected_product = ProductDetail.objects.get(id=product_id)

        if 'search' in request.POST:
            search_data = request.POST.get("search_data")

            if search_data:
                # Call the search_result function and pass the data
                return search_result(request, search_data)
            else:
                return redirect(shop)
        else:
            categories = ProductCategory.objects.filter()
            context = {
                'title': 'Shop - Product details',
                'categories': categories,
                'p_data': selected_product,
            }
            return render(request, 'main/product_details.html', context)
    else:
        messages.error(request, ('Product not found'))
        return redirect(shop)



def shop_cart(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        # get data from cart
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = 0
        for product_id, item in cart.items():
            p_data = ProductDetail.objects.get(id=int(product_id))
            item['p_data'] = p_data
            item['subtotal'] = p_data.product.price * item['quantity']
            total_price += item['subtotal']
            cart_items.append(item)

        # update cart values
        if 'update_cart' in request.POST:
            for item in cart_items:
                new_quantity = int(request.POST.get(f'quantity_{{item.p_data.id}}', 0))
                if new_quantity > 0:
                    item['quantity'] = new_quantity
                    item['subtotal'] = p_data.product.price * item['quantity']
                else:
                    if str(p_data.id) in cart:
                        del cart[str(p_data.id)]

            request.session['cart'] = cart
            return redirect(shop_cart)

        else:
            # return the value to template
            context ={
                'title': 'Shop - Cart',
                'cart_items': cart_items,
                'total_price': total_price,
                'my_cart': cart
            }
            return render(request, 'main/shop_cart.html', context)



def addToCart(request, product_id):
    product = ProductDetail.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id), {'quantity': 0})
    cart_item['quantity'] += 1
    cart[str(product_id)] = cart_item
    request.session['cart'] = cart
    return redirect(shop_cart)



def removeFromCart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect(shop_cart)



def shop_checkout(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        return render(request, 'main/checkout.html')



def order_confirmation(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        cart = request.session.get('cart', {})
        # Implement order submission logic here
        # Clear the cart after order submission
        request.session['cart'] = {}
        messages.success(request, ('Order submitted successfully!'))
        return render(request, 'main/confirmation.html')



def order_tracking(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        return render(request, 'main/tracking.html')



def client_login(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        return render(request, 'main/login.html')



def client_register(request):
    if 'search' in request.POST:
        search_data = request.POST.get("search_data")

        if search_data:
            # Call the search_result function and pass the data
            return search_result(request, search_data)
        else:
            return redirect(shop)
    else:
        return render(request, 'main/register.html')