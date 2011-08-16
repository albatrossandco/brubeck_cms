from brubeck.voxpopuli.models import Survey, Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice

admin.site.register(Survey)

class PollAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
admin.site.register(Poll, PollAdmin)
