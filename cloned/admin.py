from django.contrib import admin
from .models import Tweet, Comment, Tag
# Register your models here.


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 3

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
      (None,                {'fields': ['author', 'tweet']}),
      #('Date information', {'fields': ['date_created']}),
      ('Tags', {'fields': ['tags'] })
    ]
    inlines = [CommentInLine]
    list_display = ('author', 'tweet', 'date_created', 'date_updated')
    list_filter = ['date_created']
    search_fields = ['tweet']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('author', 'tweet', 'tags')}
        ),
    )


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Tag)
#admin.site.register(Comment)