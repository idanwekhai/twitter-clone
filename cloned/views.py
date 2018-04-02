from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import generic
#from django.views.generic.detail import SingleObjectMixin
from .models import Tweet, Comment
from django.db.models import F
from .forms import CommentForm


class TweetListView(generic.ListView):
    model = Tweet
    template_name = 'cloned/home.html'
    context_object_name = 'tweets'

class TweetAddView(generic.edit.CreateView):
    model = Tweet
    template_name = 'cloned/add_tweet.html'
    fields = ['author','tweet']

class CommentAdd(generic.FormView):
    #model = Tweet
    #context_object_name = 'tweet'
    form_class = CommentForm
    template_name = 'cloned/add_comment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        tweet = get_object_or_404(Tweet, pk=kwargs.get('pk'))
        comments = tweet.comment_set.all()
        return render(request, self.template_name, {'form': form, 'tweet':tweet, 'comments':comments})

    def post(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs.get('pk'))
        comments = tweet.comment_set.all()
        form = self.form_class(request.POST)
        comment = Comment(comment_author=form['comment_author'].value(), comment_text=form['comment_text'].value())
        if form.is_valid():
            add_comment_to_tweet = tweet.comment_set.add(comment, bulk=False)
            # <process form cleaned data>
            return HttpResponseRedirect(reverse('cloned:add_comment', args=(tweet.pk,)))

        return render(request, self.template_name, {'form': form})

# def CommentAdd(request, pk):
#     tweet = get_object_or_404(Tweet, pk=pk)
#     comments = tweet.comment_set.all()
#     comment_form = CommentForm(request.POST or None)
#     if comment_form.is_valid():
#         comment = Comment(comment_author=comment_form['comment_author'].value(), comment_text=comment_form['comment_text'].value())
#         tweet_in = tweet.comment_set.add(comment, bulk=False)
#         return HttpResponseRedirect(reverse('cloned:add_comment', args=(tweet.pk,)))
#     return render(request, 'cloned/add_comment.html', {'tweet':tweet, 'comments':comments, 'form': comment_form})


def tweet_like(request, pk):
    # for k, v in kwargs.items():
    #     if "pk" in k:
    #         tweet_pk = v
    try:
       tweet = get_object_or_404(Tweet, pk=pk)
    except (KeyError, Tweet.DoesNotExist):
        return render(request, 'cloned/home.html')
    else:
        tweet.tweet_likes = F('tweet_likes') + 1
        tweet.save()
        return HttpResponseRedirect(reverse('cloned:home'))
