from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, default='Write Short About You')
    phone = models.PositiveIntegerField(null=True, blank=True)
    follower = models.ManyToManyField(User, related_name='follower', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username

    @receiver(signal=post_save, sender=User)
    def save_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile(user=kwargs['instance'])
            user_profile.save()
