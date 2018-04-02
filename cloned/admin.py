from django.contrib import admin
from .models import Tweet, Comment
# Register your models here.


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 3

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
      (None,                {'fields': ['tweet']}),
      ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInLine]
    list_display = ('tweet', 'author', 'date', 'tweet_likes')
    list_filter = ['date']
    search_fields = ['tweet']


admin.site.register(Tweet, TweetAdmin)
#admin.site.register(Comment)