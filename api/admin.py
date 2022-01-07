from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Author, Review, Tracker, Genre, Tag


admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
admin.site.register(Tracker)
admin.site.register(Genre)
admin.site.register(Tag)