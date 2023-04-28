from django.urls import path

from API.v1.views import API_Book, API_UserOrder, UserOrdersListView
from API.v1.views import API_Author
from API.v1.views import API_Order
from API.v1.views import API_User
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', API_Book, basename='book')
router.register(r'author', API_Author, basename='author')
router.register(r'order', API_Order, basename='order')
router.register(r'user', API_User, basename='user')
urlpatterns = [
    path('user/<user_id>/order/<int:pk>', API_UserOrder.as_view()),
    path('user/<user_id>/order/', UserOrdersListView.as_view()),
]
urlpatterns.extend(router.urls)
