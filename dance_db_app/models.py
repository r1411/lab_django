from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=256)
    country = models.CharField(max_length=100)
    birthday = models.DateField()

    def get_tracks_count(self):
        return self.track_set.count()

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=256)
    duration = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist.name + ' - ' + self.title

class Dance(models.Model):
    title = models.CharField(max_length=256)
    difficulty = models.IntegerField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
