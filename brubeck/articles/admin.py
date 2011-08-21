from brubeck.articles.models import Article, Correction
from django.contrib import admin

class CorrectionInline(admin.StackedInline):
    model = Correction

class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None, {
            'fields': ('title', 'cdeck', 'blurb', 'pub_date', 'byline', 'static_byline',)
        }),
        ("Publishing data", {
            'fields': ('is_published', 'type', 'priority', 'updated', 'issue', 'section', 'tags', 'enable_comments')
        }),
        ("Main content", {
            'fields': ('body', 'photos', 'graphics')
        }),
        ("Other attached content", {
            'classes': ('collapse',),
            'fields': ('sidebar', 'videos', 'slideshows', 'audio_clips', 'podcast_episodes', 'attached_files', 'editorial_cartoons', 'calendar', 'map', 'polls', 'teaser_photo')
        }),
        ("Don't touch unless you know what you're doing", {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
    filter_horizontal = ('photos', 'editorial_cartoons', 'graphics', 'attached_files', 'videos', 'slideshows', 'audio_clips', 'podcast_episodes', 'tags', 'polls')
    inlines = (CorrectionInline,)
    list_display = ('title', 'pub_date', 'section', 'is_published', 'priority')
    list_editable = ('priority', 'is_published')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('byline',)
    search_fields = ('title', 'body', 'cdeck', 'blurb')
admin.site.register(Article, ArticleAdmin)
