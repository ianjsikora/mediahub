from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

class Character(models.Model):
    name = models.CharField(max_length=100)
    tomato_id = models.IntegerField()

    def __unicode__(self):
        return unicode(self.name)


class Content(models.Model):
    title = models.CharField(max_length=100)
    TYPE_CHOICES = {
        ('movie' , 'Movie'),
        ('series', 'TV Series'),
    }
    type = models.CharField(max_length=6,choices=TYPE_CHOICES,default='movie')
    release_date = models.DateField()
    runtime = models.IntegerField()
    rating = models.CharField(max_length=10)
    genre = models.ManyToManyField(Genre)
    synopsis = models.TextField()
    rating_tomato_c = models.IntegerField()
    rating_tomato_a = models.IntegerField()
    rating_imdb = models.FloatField(null=True)
    poster = models.URLField()
    tomato_id = models.IntegerField()
    IMDb_id = models.CharField(max_length=30, null=True)
    IMDB_url = models.URLField()
    cast = models.ManyToManyField(Character)

    def __unicode__(self):
        return unicode(self.title)

class Person(models.Model):
    name = models.CharField(max_length=100)
    TYPE_CHOICES = {
        ('actor' , 'Actor'),
        ('director', 'Director'),
        ('writer', 'Writer'),
    }
    type = models.CharField(max_length=10,choices=TYPE_CHOICES,default='actor')
    birthday = models.DateField(null=True)
    headshot = models.URLField(default='https://ivegotaproblemblog.files.wordpress.com/2012/07/386px-tux-g2-svg1.png')
    tomato_id = models.IntegerField()
    roles = models.ManyToManyField(Character)

    def __unicode__(self):
        return self.name
