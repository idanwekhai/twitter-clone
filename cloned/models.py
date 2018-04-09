from django.db import models
from django.urls import reverse
from django.utils import timezone
from profiles.models import Profile
# Create your models here

class Tweet(models.Model):
    #Number of likes for a particular tweeet
    #tweet_likes = models.IntegerField(default=0)
    #name of the person who posted a tweet

    author  = models.ForeignKey(
        'accounts.User',
        related_name='tweets',
        on_delete=models.CASCADE,)

    #The date a tweet is posted
    date_created = models.DateTimeField(auto_now_add=True)
    #The body of the tweet
    tweet = models.TextField(max_length=150)

    tags = models.ManyToManyField(
        'cloned.Tag',
        related_name='tweets')
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Tweets'
        ordering = ['-date_created', ]
    
    
    def get_absolute_url(self):
        return reverse('cloned:home')

    def __str__(self):
        return self.tweet

class Comment(models.Model):
    #make the relationship btw the teeet and the comment
    comment_for = models.ForeignKey(
        'cloned.Tweet',
        on_delete=models.CASCADE,
        related_name='comments')

    #name/author of the person commenting
    comment_author = models.ForeignKey(
        'accounts.User',
        related_name='comments',
        on_delete=models.CASCADE)
    #body of the comment
    comment_text = models.TextField(max_length=250)
    #the nunber of likes a tweet has
    #comment_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text

class Like(models.Model):
    tweet = models.ForeignKey(Tweet,
        related_name='liked_tweet',
        on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User',
        related_name='liker',
        on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def like(self, tweet):
        """Like tweet is we are not alredy liking it"""
        self.tweet.add(tweet)

    def unlike(self, tweet):
        """Unlike tweet if we are already liking it"""
        self.tweet.remove(tweet)

    def has_liked(self, tweet):
        """retruns True if we have alreay liked a tweet, otherwise False"""
        return self.tweet.filter(pk=tweet.pk).exists()

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)


class Tag(models.Model):
    tag = models.CharField(max_length=150)

    def __str__(self):
        return self.tag