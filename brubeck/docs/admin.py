from brubeck.docs.models import BookType, Book, Entry, Example
from django.contrib import admin

class BookTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )
admin.site.register(BookType)

class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'pub_date', 'contributors')
        }),
        ("Publishing data", {
            'fields': ('type', 'priority', 'is_update', 'publication', 'site', 'volume', 'is_archived')
        }),
        ("Main content", {
            'fields': ('introductory_message', 'pdf')
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
    filter_horizontal = ('contributors', 'publication', 'site', 'volume')
admin.site.register(Book, BookAdmin)

class EntryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'book', 'tags', 'order_by')
        }),
        ("Main content", {
            'fields': ('text', 'justification')
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )
admin.site.register(Entry, EntryAdmin)

admin.site.register(Example)
