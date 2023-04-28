from django.urls import path
from .views import create_order, all_orders, remove_order


urlpatterns = [
    path('orders/', all_orders, name='all_orders'),
    path('create_order/', create_order, name='create_order'),
    path('remove_order/<int:id>', remove_order, name='remove_order'),
]