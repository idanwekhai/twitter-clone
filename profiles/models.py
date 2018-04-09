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

    