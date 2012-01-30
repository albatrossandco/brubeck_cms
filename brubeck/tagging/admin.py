from brubeck.tagging.models import Tag
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'last_updated',)
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('last_updated',)
admin.site.register(Tag, TagAdmin)
