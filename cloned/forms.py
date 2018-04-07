from django import forms
from .models import Tweet, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['comment_author']
        fields = ('comment_text',)

    # def save(self, request, pk):
    #     q = Tweet.objects.get(pk=pk)
    #     q.comment_set.create(comment_author=name, comment_text=comment)
    #     q.save()
    #     return q


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ['author']
        fields = ['tweet']
