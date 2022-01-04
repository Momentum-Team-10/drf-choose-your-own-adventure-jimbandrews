from rest_framework import serializers
from .models import User, Book, Author, Review, Tracker, Tag, Genre


class AuthorForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'pk',
            'name',
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorForBookSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
            'author',
            'featured',
        )