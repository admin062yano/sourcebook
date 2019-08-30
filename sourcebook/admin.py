from django.contrib import admin
from sourcebook.models import Book, Page, Source

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name') 

admin.site.register(Book, BookAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'book')
    list_display_links = ('id', 'name')

admin.site.register(Page, PageAdmin)