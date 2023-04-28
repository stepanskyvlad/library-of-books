from django.contrib import admin
from author.admin import MembershipInline
from .models import Book


class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'count', 'view_authors',)
    list_filter = ('id', 'name', 'authors')
    fieldsets = (
        ('Information that does not change', {
            'fields': ('name', 'description')
        }),
        ('Information that changes', {
            'fields': ('count',),
        }),
    )
    inlines = [
        MembershipInline,
    ]

    @staticmethod
    def view_authors(obj):
        return "\n".join([author.name for author in obj.authors.all()])


admin.site.register(Book, BookAdmin)
