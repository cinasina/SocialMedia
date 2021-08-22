from django.db import models
from django.contrib.auth.models import User
from Post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    self_cm = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.text[:15]}'

    class Meta:
        ordering = ('-created',)
