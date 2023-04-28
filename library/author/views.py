from django.shortcuts import render, redirect
from author.models import Author
from django.contrib import messages
from .forms import NewAuthor


def all_authors(request):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        return render(request, 'authors.html', {'data': Author.objects.all()})
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")


def create_author(request):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        if request.method == 'POST':
            form = NewAuthor(request.POST)
            print(form.data)
            user = Author.create(
                name=form.data.get("first_name"),
                surname=form.data.get("last_name"),
                patronymic=form.data.get("patronymic"),
            )

            if isinstance(user, str):
                messages.error(request, f'ERROR! {user}')
                return redirect("/author/create_author")

            messages.success(request, f'Success! Author was created!')

            return redirect("/author/authors")
        else:
            form = NewAuthor()
            return render(request, 'new_author.html', {'form': form})
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")


def remove_author(request, id):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        if not Author.get_by_id(id).books.all():
            if Author.delete_by_id(id):
                messages.success(request, f'Success! Author was deleted!')
                return redirect("/author/authors")
            else:
                messages.error(request, f'ERROR! Something went wrong!')
                return redirect("/author/authors")
        else:
            messages.error(request, f'ERROR! You cannot delete an author who has books!')
            return redirect("/author/authors")
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")
