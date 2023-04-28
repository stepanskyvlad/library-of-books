from django.shortcuts import render, redirect
from authentication.models import CustomUser
from order.models import Order
from book.models import Book
from django.contrib import auth, messages
from authentication.forms import LogInForm, SignInForm


def sign_up(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            user = CustomUser.create(
                first_name=form.cleaned_data['first_name'],
                middle_name=form.cleaned_data['middle_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                role=int(form.cleaned_data['role'][0])
            )

            if isinstance(user, str):
                messages.error(request, f'ERROR! {user}')
                return redirect("/authentication/sign_up")

            auth.login(request, user)
            messages.success(request, f'Success! You are logged in!')

            return redirect("/")
        else:
            messages.error(request, f'ERROR! {form.errors}')
            return render(request, 'sign_up.html', {'form': form})
    else:
        return render(request, 'sign_up.html', {'form': SignInForm()})


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)

        if form.is_valid():
            user = CustomUser.get_by_email(
                email=form.cleaned_data['email']
            )

            if user:
                if user.password == form.cleaned_data['password']:
                    pass
                else:
                    messages.error(request, f'ERROR! Incorrect password!')
                    return redirect("/authentication/log_in")
            else:
                messages.error(request, f'ERROR! The user does not exist, please sign up!')
                return redirect("/authentication/log_in")

            auth.login(request, user)
            messages.success(request, f'Success! You are logged in!')

            return redirect("/")
        else:
            messages.error(request, f'ERROR! {form.errors}')
            return render(request, 'log_in.html', {'form': form})
    else:
        return render(request, 'log_in.html', {'form': LogInForm()})


def log_out(request):
    auth.logout(request)
    messages.success(request, f'Success! You are logged out!')

    return redirect("/")


def all_users(request):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        return render(request, 'users.html', {'data': CustomUser.objects.all()})
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")


def user(request, id):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser or (request.user.is_authenticated and request.user.id == id):
        book_list = []
        for order in Order.objects.all():
            if order.user_id == id and not order.end_at:
                book_dict = {}
                book_dict["book_id"] = order.book_id
                book_dict["book_name"] = Book.get_by_id(order.book_id).name
                for author in Book.get_by_id(order.book_id).authors.all():
                    book_dict["author_full_name"] = f"{author.name} {author.patronymic} {author.surname}"
                book_list.append(book_dict)

        return render(request, 'user.html', {'selected_user': CustomUser.get_by_id(id), 'books': book_list})
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")
