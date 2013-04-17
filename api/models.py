from django.db import models
from django.contrib.auth.models import User

class UserAccessToken(models.Model):
    user = models.ForeignKey(User, unique=True)
    access_token = models.TextField()
    expires = models.BigIntegerField()

    def __unicode__(self):
        return "UserAccessToken"
  

class FacebookProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    access_token = models.TextField()
    expires = models.BigIntegerField()

    def __unicode__(self):
        return "FacebookProfile"
  
  
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    blurb = models.CharField(max_length=255)
    avatar_url = models.TextField()

    def __unicode__(self):
        return "UserProfile"


