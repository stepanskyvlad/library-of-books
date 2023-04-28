from django.shortcuts import render, redirect
from book.models import Book
from authentication.models import CustomUser
from order.models import Order
import datetime
from django.contrib import messages
from .forms import OrderForm


def all_orders(request):
    if request.user.is_authenticated:
        order_list = []
        for order in Order.objects.all():
            if (request.user.role == 1 or request.user.is_superuser) or order.user_id == request.user.id:
                order_dict = {}
                order_dict["id"] = order.id
                order_dict["book_name"] = Book.get_by_id(order.book_id).name
                user = CustomUser.get_by_id(order.user_id)
                order_dict["user_full_name"] = f"{user.first_name} {user.middle_name} {user.last_name}"
                order_dict["end_at"] = order.end_at
                order_dict["created_at"] = order.created_at
                order_dict["plated_end_at"] = order.plated_end_at
                order_list.append(order_dict)

        return render(request, 'order/orders.html', {'data': order_list})
    else:
        messages.error(request, f'ERROR! Only authorized users!')
        return redirect("/")


def create_order(request):
    USERS = [(user.id, f'{user.first_name} {user.last_name}') for user in CustomUser.objects.all()]
    BOOKS = [(book.id, f'{book.name}') for book in Book.objects.all()]
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            form.fields['user'].choices = USERS
            form.fields['book'].choices = BOOKS
            order = Order.create(
                user=CustomUser.get_by_id(int(form.data.get('user'))) if request.user.role == 1 else CustomUser.get_by_id(request.user.id),
                book=Book.get_by_id(int(form.data.get('book'))),
                plated_end_at=datetime.datetime.strptime(form.data.get('plated_end_at'), '%Y-%m-%dT%H:%M')
            )

            if isinstance(order, str):
                messages.error(request, f'ERROR! {order}')
                return redirect("/order/create_order")

            messages.success(request, f'Success! Order was created!')

            return redirect("/order/orders")
        else:
            form = OrderForm()
            form.fields['user'].choices = USERS
            form.fields['book'].choices = BOOKS
            if request.user.role == 0:
                form.fields['user'].initial = request.user.id
                form.fields['user'].disabled = True
                form.fields['user'].label = 'Selected User'
            current_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
            return render(request, 'order/create_order.html', {'users': CustomUser.objects.all(),
                                                               'books': Book.objects.all(),
                                                               'current_time': current_time,
                                                               'form': form})
    else:
        messages.error(request, f'ERROR! Only authorized users!')
        return redirect("/")


def remove_order(request, id):
    if (request.user.is_authenticated and request.user.role == 1) or request.user.is_superuser:
        order = Order.get_by_id(id)
        if order:
            order.end_at = datetime.datetime.now()
            order.book.count += 1
            order.book.save()
            order.save()
            messages.success(request, f'Success! Order was closed!')
            return redirect("/order/orders")
        else:
            messages.error(request, f'ERROR! Something went wrong!')
            return redirect("/order/orders")
    else:
        messages.error(request, f'ERROR! Librarians and superusers only!')
        return redirect("/")
