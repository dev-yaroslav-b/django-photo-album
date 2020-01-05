import os

from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class MediaPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    media = models.FileField(upload_to=user_directory_path)
    created_date = models.DateTimeField(auto_now_add=False)

    def extension(self):
        name, extension = os.path.splitext(self.media.name)
        if extension in ['.jpg', '.jpeg','.png']:
            return 'img'
        elif extension in ['.mp4', '.mkv']:
            return 'video'
        else:
            None

    class Meta:
        ordering = ('title', 'created_date')

    def __str__(self):
        return self.title
