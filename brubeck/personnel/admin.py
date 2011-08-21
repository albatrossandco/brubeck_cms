from brubeck.personnel.models import Staffer, Position, Tenure
from django.contrib import admin

class TenureInline(admin.TabularInline):
    model = Tenure

class StafferAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('first_name', 'middle_name', 'last_name')
        }),
        ("Extra information", {
            'fields': ('is_active', 'email', 'mugshot', 'user')
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )
    inlines = (TenureInline,)
    list_display = ('last_name', 'first_name', 'middle_name', 'email')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
admin.site.register(Staffer, StafferAdmin)

admin.site.register(Position)
