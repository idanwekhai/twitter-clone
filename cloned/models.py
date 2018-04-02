from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here

class Tweet(models.Model):
    #Number of likes for a particular tweeet
    tweet_likes = models.IntegerField(default=0)
    #name of the person who posted a tweet
    author  = models.CharField(max_length=100)
    #The date a tweet is posted
    date = models.DateField(default=timezone.now)
    #The body of the tweet
    tweet = models.TextField(max_length=150)
    
    def get_absolute_url(self):
        return reverse('cloned:home')

    def __str__(self):
        return self.tweet

class Comment(models.Model):
    #the relationship btw the teeet ant the comment
    comment_for = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    #name/author of the person commenting
    comment_author = models.CharField(max_length=100)
    #body of the comment
    comment_text = models.TextField(max_length=250)
    #the nunber of likes a tweet has
    comment_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text