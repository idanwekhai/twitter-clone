from django.db import models
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    #there is a relation ship between the the user and a profile
    #every user must have one profile
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)

    #A filed totell other users about them
    #This field is initially blank so blank=True
    bio = models.TextField(blank=True)
    #image = models.ImageField(blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

    

class Connection(models.Model):
    follower = models.ForeignKey('profiles.Profile',
        related_name='follower',
        on_delete=models.CASCADE)
    following = models.ForeignKey('profiles.Profile',
        related_name='following',
        on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def follow(self, profile):
        """"follow profile if we are not already folowing it"""
        self.following.add(profile)

    def unfollow(self, profile):
        """"unfollow profile if we are already folowing it"""
        self.following.remove(profile)

    def is_following(self, profile):
        """returns True if we are following a profile, otherwise False"""
        return self.following.filter(pk=profile.pk).exists()
 
    def is_followed_by(self, profile):
        """Returns True is a profile is following us, otherwise False"""
        return self.follower.filter(pk=profile.pk).exists()

    def __str__(self):
        return "{} : {}".format(self.follower.username, self.following.username)