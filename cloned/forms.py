from django import forms
from .models import Tweet, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_author']
        fields = ('comment_text',)


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ['author']
        fields = ['tweet']
