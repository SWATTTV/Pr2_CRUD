from django.contrib import admin
from .models import Author, Category, Publisher, ReadingRoom, Book, Reader, Librarian, Loan


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_year', 'copies')
    search_fields = ('title', 'isbn')
    list_filter = ('category', 'publisher')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'issue_date', 'due_date', 'returned')
    list_filter = ('returned',)


admin.site.register([Author, Category, Publisher, ReadingRoom, Reader, Librarian])
