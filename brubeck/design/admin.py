from brubeck.design.models import Graphic, Layout
from django.contrib import admin

admin.site.register(Graphic)

class LayoutAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'pub_date', 'byline', 'static_byline', 'PDF')
        }),
        ("Publishing data", {
            'fields': ('is_published', 'issue', 'section', 'first_page', 'last_page', 'type')
        }),
        ("Related content", {
            'fields': ('articles', 'photos', 'graphics')
        })
    )
admin.site.register(Layout, LayoutAdmin)
