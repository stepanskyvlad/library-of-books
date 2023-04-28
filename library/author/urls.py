from django.urls import path
from .views import all_authors, create_author, remove_author


urlpatterns = [
    path('authors/', all_authors, name='all_authors'),
    path('create_author/', create_author, name='create_author'),
    path('remove_author/<int:id>', remove_author, name='remove_author'),
]
