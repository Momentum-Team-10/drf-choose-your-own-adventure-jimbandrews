from typing import List
from django.db.models.base import Model
from django.shortcuts import render
from .models import Book, Author, Review
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_name = self.request.data['author']
        author, created = Author.objects.get_or_create(name=author_name)
        serializer.save(author=author, added_by=self.request.user)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book=self.kwargs['book_pk'])

    def perform_create(self, serializer):
        book = Book.objects.get(pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)


class AuthorViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class FeaturedBooksListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(featured=True)
        return queryset