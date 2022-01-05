from django.db.models.base import Model
from django.shortcuts import render
from .models import Book, Author
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_name = self.request.data['author']
        author = Author.objects.get(name=author_name)
        serializer.save(author=author)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
