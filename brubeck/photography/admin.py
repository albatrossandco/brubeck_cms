from brubeck.photography.models import Photo
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'pub_date', 'byline', 'static_byline', 'image', 'cutline')
        }),
        ("Publishing data", {
            'fields': ('is_published', 'issue', 'section', 'tags', 'enable_comments', 'mugshot', 'illustration')
        }),
    )
    filter_horizontal = ('byline', 'tags',)
admin.site.register(Photo, PhotoAdmin)
