from django.db import models
from django.contrib.auth.models import User
from Profile.models import Profile


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_following = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.follower} Is Following {self.following}'
