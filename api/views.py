from django.db.models.base import Model
from django.shortcuts import render
from .models import Book, Author
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
