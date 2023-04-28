from rest_framework import serializers
from book.models import Book
from author.models import Author
from order.models import Order
from authentication.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "name", "description", "count")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "surname", "patronymic", "books")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "book", "user", "created_at", "end_at", "plated_end_at")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "created_at",
            "updated_at",
            "role",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_active",
        )


class UserOrdersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", 'book', 'created_at', 'end_at', 'plated_end_at']