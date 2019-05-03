from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=(self.pk,))


    def snippet(self):
        if Post.content == [50]:
            return self.content[50]
        else:
            return self.content[:50] + '...'

class User(Post, models.Model):
    user = User

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('user-profile', args=(self.pk))
