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
    WANT = 'WANT'
    READING = 'READ'
    DONE = 'DONE'
    STATUS_CHOICES = [
        (WANT, 'Want to Read'),
        (READING, 'Currently Reading'),
        (DONE, 'Finished Reading'),
    ]
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default=WANT,
    )
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tracker')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='tracker')


class Genre(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField('Book', related_name='genres', blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField('Book', related_name='tags', blank=True)