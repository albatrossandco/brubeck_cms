from brubeck.tagging.models import Tag
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Tag, TagAdmin)