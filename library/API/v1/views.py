from rest_framework import viewsets, generics

from book.models import Book
from author.models import Author
from order.models import Order
from authentication.models import CustomUser
from API.v1.serializer import BookSerializer, UserOrdersListSerializer
from API.v1.serializer import AuthorSerializer
from API.v1.serializer import OrderSerializer
from API.v1.serializer import UserSerializer


class API_Book(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class API_Author(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class API_Order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class API_User(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class API_UserOrder(generics.RetrieveDestroyAPIView):
    lookup_field = "pk"
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.kwargs["pk"]:
            return Order.objects.filter(user_id=self.kwargs['user_id'])
        else:
            return Order.objects.all()


class UserOrdersListView(generics.ListAPIView):
    serializer_class = UserOrdersListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=kwargs['user_id'])
        return self.list(request, *args, **kwargs)
