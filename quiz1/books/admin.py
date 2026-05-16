from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "rating", "is_featured")
    list_filter = ("is_featured",)
    search_fields = ("title", "author")
