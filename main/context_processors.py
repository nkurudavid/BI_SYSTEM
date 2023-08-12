from .models import ProductDetail

# context_processors.py
def cart_context(request):
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
    return {'cart_items': cart_items, 'total_price': total_price,}