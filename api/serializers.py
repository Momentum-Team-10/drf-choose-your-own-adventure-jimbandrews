from rest_framework import serializers
from .models import User, Book, Author, Review, Tracker, Tag, Genre


class AuthorForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'pk',
            'name',
        )


class GenreForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'pk',
            'name',
        )


class TagForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'pk',
            'name',
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorForBookSerializer(many=True, read_only=True)
    genres = GenreForBookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
            'author',
            'featured',
            'genres',
            'tags',
            'reviews',
        )


class BookForAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
        )


class AuthorSerializer(serializers.ModelSerializer):
    books = BookForAuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = (
            'pk',
            'name',
            'books',
        )