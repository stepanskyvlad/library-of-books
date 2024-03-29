from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')
    list_filter = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')
    fieldsets = (
        ('Chose a user and a book', {
            'fields': (('user', 'book'),)
        }),
        ('Chose the date', {
            'fields': (('end_at', 'plated_end_at'),),
        }),
    )


admin.site.register(Order, OrderAdmin)
