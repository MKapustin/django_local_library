from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

#admin.site.register(Author)
class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(BookInstance)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'borrower', 'due_back', 'book', 'is_overdue')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            "fields": (
                'book',
                'imprint',
                'id'
            ),
        }),
        ('Availability', {
            'fields': (
                'status',
                'due_back',
                'borrower'
            )
        })
    )
    

admin.site.register(Genre)

