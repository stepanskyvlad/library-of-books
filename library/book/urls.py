from django.urls import path
from .views import all_books, create_book, book, all_books_filter, remove_book


urlpatterns = [
    path('create_book/', create_book, name='create_book'),
    path('remove_book/<int:id>', remove_book, name='remove_book'),
    path('<int:id>/', book, name='book'),
    path('all_books/', all_books, name='all_books'),
    path('all_books/<str:type_of>', all_books, name='all_books_order'),
    path('all_books/filter/', all_books_filter, name='all_books_filter')
]
