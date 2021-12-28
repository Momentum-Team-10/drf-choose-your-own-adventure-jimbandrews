from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image_url = models.URLField()

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

