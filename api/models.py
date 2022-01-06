from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image_url = models.URLField()

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book')
        ]

    title = models.CharField(max_length=250)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    pub_year = models.IntegerField(null=True)
    featured = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='added_books', null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    tags = models.ManyToManyField('Tag', related_name='books', blank=True)

    def __repr__(self):
        return f"<Book name={self.title}>"

    def __str__(self):
        return self.title


class Author(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_author')
        ]

    name = models.CharField(max_length=150)

    def __repr__(self):
        return f"<Author name={self.name}>"

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<Review user={self.user.username} book={self.book.title}>"

    def __str__(self):
        return self.created


class Tracker(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_tracker')
        ]

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

    def __repr__(self):
        return f"<Tracker user={self.user.username} book={self.book.title}>"

    def __str__(self):
        return self.user


class Genre(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_genre')
        ]

    name = models.CharField(max_length=150)

    def __repr__(self):
        return f"<Genre name={self.name}>"

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_tag')
        ]

    name = models.CharField(max_length=150)

    def __repr__(self):
        return f"<Tag name={self.name}>"

    def __str__(self):
        return self.name