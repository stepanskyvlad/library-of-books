from django.contrib import admin
from .models import Author


class MembershipInline(admin.TabularInline):
    model = Author.books.through


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'surname', 'patronymic', 'view_books')
    list_filter = ('id', 'name', 'surname', 'patronymic', 'books')
    fields = ('name', ('surname', 'patronymic'))
    inlines = [
        MembershipInline,
    ]
    exclude = ('books',)

    @staticmethod
    def view_books(obj):
        return "\n".join([book.name for book in obj.books.all()])


admin.site.register(Author, AuthorAdmin)
