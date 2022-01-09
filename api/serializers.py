from rest_framework import serializers
from rest_framework.relations import StringRelatedField
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


class ReviewSerializer(serializers.ModelSerializer):
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
    status = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = (
            'pk',
            'title',
            'author',
            'pub_year',
            'genres',
            'tags',
            'status',
            'reviews',
        )

    def get_status(self, obj):
        # grab user making request from serializer context
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        else:
            return "None"
        
        # check if tracker object exists and returns it
        tracker = Tracker.objects.filter(book=obj, user=user)
        if tracker.exists():
            return str(tracker[0])
        return "None"


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


class TrackerSerializer(serializers.ModelSerializer):
    user = UserNestedSerializer(read_only=True)
    book = BookForReviewSerializer(read_only=True)
    class Meta:
        model = Tracker
        fields = (
            'pk',
            'user',
            'book',
            'status',
        )