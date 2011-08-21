from brubeck.publishing.models import Publication, Section, Volume, Issue
from django.contrib import admin

admin.site.register(Publication)

class SectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'publication')
        }),
        ("Publishing data", {
            'fields': ('priority', 'is_archived')
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )
    list_display = ('name', 'publication', 'priority', 'is_archived')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Section, SectionAdmin)

admin.site.register(Volume)

class IssueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('volume', 'issue_id', 'pub_date', 'online_update')
        }),
        ("Issue PDF information", {
            'fields': ('render_issue_pdf', 'issue_pdf_link', 'submit_to_issuu', 'issuu_id', 'pdf_converted')
        }),
    )
admin.site.register(Issue)
