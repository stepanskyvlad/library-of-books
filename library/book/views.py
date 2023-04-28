from .forms import SearchBooks
from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages
from author.models import Author
from order.models import Order
from django.db.models import Q
from .forms import BookForm


def get_queryset(word):
    object_list = Book.objects.filter(
        Q(name__icontains=word) | Q(description__icontains=word) | Q(count__icontains=word) | Q(id__icontains=word) |
        Q(authors__name__icontains=word) | Q(authors__surname__icontains=word) | Q(authors__patronymic__icontains=word)
    )

    return object_list


def all_books_filter(request):
    if request.method == 'POST':
        form = SearchBooks(request.POST)
        if form.is_valid():
            spec_int = None
            if form.cleaned_data['word'].isdigit():
                spec_int = form.cleaned_data['word']

            return render(request, 'book/books.html', {'data': get_queryset(request.POST['word']),
                                                       'spec_word': form.cleaned_data['word'],
                                                       'spec_int': spec_int, 'form': form})
        else:
            messages.error(request, f'ERROR! {form.errors}')
            return render(request, 'book/books.html', {'data': Book.objects.all(), 'form': SearchBooks()})
    else:
        return render(request, 'book/books.html', {'data': Book.objects.all(), 'form': SearchBooks()})


def all_books(request, type_of=None):
    if request.user.is_authenticated:
        if type_of:
            if type_of == 'name':
                return render(request, 'book/books.html', {'data': Book.objects.all().order_by('name'),
                                                           'form': SearchBooks()})
            elif type_of == 'description':
                return render(request, 'book/books.html', {'data': Book.objects.all().order_by('description'),
                                                           'form': SearchBooks()})
            elif type_of == 'count':
                return render(request, 'book/books.html', {'data': Book.objects.all().order_by('count'),
                                                           'form': SearchBooks()})
        else:
            return render(request, 'book/books.html', {'data': Book.objects.all(), 'form': SearchBooks()})

        return render(request, 'book/books.html', {'data': Book.objects.all(), 'form': SearchBooks()})
    else:
        messages.error(request, f'ERROR! Only authorized users!')
        return redirect("/")


def book(request, id):
    if request.user.is_authenticated:
        return render(request, 'book/book.html', {'selected_book': Book.get_by_id(id)})
    else:
        messages.error(request, f'ERROR! Only authorized users!')
        return redirect("/")


def create_book(request):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        AUTHORS = [(author.id, f'{author.name} {author.surname} {author.patronymic}') for author in Author.objects.all()]
        if Author.objects.all():
            if request.method == 'POST':
                form = BookForm(request.POST)
                form.fields['author'].choices = AUTHORS
                book = Book.create(
                    name=form.data.get('name'),
                    description=form.data.get('description'),
                    count=form.data.get('count'),
                )

                if isinstance(book, str):
                    messages.error(request, f'ERROR! {book}')
                    return redirect("/book/create_book")

                book.add_authors(Author.get_by_id(form.data.get('author')))
                messages.success(request, f'Success! Books was created!')

                return redirect("/book/all_books")
            else:
                form = BookForm()
                form.fields['author'].choices = AUTHORS
                return render(request, 'book/new_book.html', {'authors': Author.objects.all(),
                    'form': form})
        else:
            messages.error(request, f'ERROR! You need create one author before that!')
            return redirect("/")
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")


def remove_book(request, id):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        for order in Order.objects.all():
            if order.book_id == id:
                messages.error(request, f'ERROR! You cannot delete a books that is in orders!')
                return redirect("/book/all_books")

        Book.delete_by_id(id)
        messages.success(request, f'Success! Books was deleted!')
        return redirect("/book/all_books")

    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")
