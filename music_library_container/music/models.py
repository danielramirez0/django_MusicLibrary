from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateTimeField()
    likes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def increment_like(self) ->int:
        self.likes +=1