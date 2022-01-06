from rest_framework import serializers
from .models import User, Book, Author, Review, Tracker, Tag, Genre


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


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


class BookForReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
            'author',
        )


class ReviewForBookSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(read_only=True)
    book = BookForReviewSerializer(read_only=True)
    class Meta:
        model = Review
        fields = (
            'pk',
            'user',
            'book',
            'created',
            'text',
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorForBookSerializer(read_only=True)
    genres = GenreForBookSerializer(many=True, read_only=True)
    tags = TagForBookSerializer(many=True, read_only=True)
    reviews = ReviewForBookSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
            'author',
            'pub_year',
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
            'pub_year'
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