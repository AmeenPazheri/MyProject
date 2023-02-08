from . import views
from django.urls import path

app_name='cart'


urlpatterns = [
    path('add/<int:product_id>/',views.addcart,name='addcart'),
    path('',views.Cart_detail,name='Cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
]