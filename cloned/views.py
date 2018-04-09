from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import F
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from braces import views

from profiles.models import Profile
from .forms import CommentForm, TweetForm
from .models import Tweet, Comment, Like

class TweetListView(generic.ListView):
    template_name = 'cloned/home.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-date_created')


class TweetEditView(views.LoginRequiredMixin, generic.edit.UpdateView):
    model = Tweet
    fields = ['tweet']
    template_name = 'cloned/tweet_edit.html'
    context_object_name = 'tweet'
    success_url = reverse_lazy('cloned:home')


class TweetAddView(views.LoginRequiredMixin, generic.edit.CreateView):
    model = Tweet
    template_name = 'cloned/add_tweet.html'
    form_class = TweetForm

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.author = Profile.objects.get(user=self.request.user)
        tweet.save()
        return HttpResponseRedirect(reverse('cloned:home'))


class CommentAddView(views.LoginRequiredMixin, generic.FormView):
    form_class = CommentForm
    template_name = 'cloned/add_comment.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        tweet = get_object_or_404(Tweet, pk=kwargs.get('pk'))
        comments = tweet.comments.all()
        return render(request, self.template_name, {'form': form, 'tweet':tweet, 'comments':comments})

    def post(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs.get('pk'))
        comments = tweet.comments.all()
        form = self.form_class(request.POST)
        comment = Comment(comment_text=form['comment_text'].value())
        comment.comment_for = tweet
        comment.comment_author = Profile.objects.get(user=self.request.user)
        if form.is_valid():
            add_comment_to_tweet = tweet.comments.add(comment, bulk=False)
            return HttpResponseRedirect(reverse('cloned:add_comment', args=(tweet.pk,)))
        return render(request, self.template_name, {'form': form})

class TweetDeleteView(iew.LoginRequiredMixin, generic.DeleteView):
    model = Tweet
    template_name = 'cloned/tweet_delete.html'
    success_url = reverse_lazy('home')

@login_required
def TweetLikeView(request, *args, **kwargs):
    try:
        tweet = Tweet.objects.get(pk=kwargs['pk'])

        _, created = Like.objects.get_or_create(tweet=post, user=request.user)

        if not created:
            messages.warning(request, 'You\'ve already liked the tweet.')
    except Post.DoesNotExist:
        messages.warning(request, 'Tweet does not exist')

    return HttpResponseRedirect(reverse_lazy('cloned:home',kwargs={'id': kwargs['id']}))


# def CommentAdd(request, pk):
#     tweet = get_object_or_404(Tweet, pk=pk)
#     comments = tweet.comment_set.all()
#     comment_form = CommentForm(request.POST or None)
#     if comment_form.is_valid():
#         comment = Comment(comment_author=comment_form['comment_author'].value(), comment_text=comment_form['comment_text'].value())
#         tweet_in = tweet.comment_set.add(comment, bulk=False)
#         return HttpResponseRedirect(reverse('cloned:add_comment', args=(tweet.pk,)))
#     return render(request, 'cloned/add_comment.html', {'tweet':tweet, 'comments':comments, 'form': comment_form})


# def tweet_like(request, pk):
#     # for k, v in kwargs.items():
#     #     if "pk" in k:
#     #         tweet_pk = v
#     try:
#        tweet = get_object_or_404(Tweet, pk=pk)
#     except (KeyError, Tweet.DoesNotExist):
#         return render(request, 'cloned/home.html')
#     else:
#         tweet.tweet_likes = F('tweet_likes') + 1
#         tweet.save()
#         return HttpResponseRedirect(reverse('cloned:home'))
