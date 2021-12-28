from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image_url = models.URLField()

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    featured = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    name = models.CharField(max_length=150)


class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)


class Tracker(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tracker')
    want = models.ManyToManyField('Book', related_name='want_to_read', blank=True)
    reading = models.ManyToManyField('Book', related_name='reading', blank=True)
    finished = models.ManyToManyField('Book', related_name='finished', blank=True)


class Genre(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField('Book', related_name='genres', blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField('Book', related_name='tags', blank=True)