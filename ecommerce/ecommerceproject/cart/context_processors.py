from .models import Cart,CartItems
from .views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cart_items=CartItems.objects.all().filter(cart=cart[:1])
            for items in cart_items:
                item_count += items.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)