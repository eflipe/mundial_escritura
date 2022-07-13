from django.db import models
from django.contrib.auth.models import User


class SongInfo(models.Model):
    song_title = models.CharField(max_length=222, unique=True)
    song_lyrics = models.TextField(max_length=5000)
    song_video_url = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Songs Info'

    def __str__(self):
        return self.song_title


class Stories(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    id_songs = models.ForeignKey(SongInfo, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.author.username
