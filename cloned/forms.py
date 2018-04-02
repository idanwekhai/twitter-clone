from django import forms
from .models import Tweet, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # name = forms.CharField()
        # comment = forms.CharField(widget=forms.Textarea)
        fields = ('comment_author', 'comment_text')

    # def save(self, request, pk):
    #     q = Tweet.objects.get(pk=pk)
    #     q.comment_set.create(comment_author=name, comment_text=comment)
    #     q.save()
    #     return q
