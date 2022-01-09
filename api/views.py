from .models import Book, Author, Review, Tracker
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer, TrackerSerializer
from .permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
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

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        elif self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book=self.kwargs['book_pk'])

    def perform_create(self, serializer):
        book = Book.objects.get(pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)

    def get_permissions(self):
        safe = ('GET', 'HEAD', 'OPTIONS')
        author_methods = ('PATCH', 'PUT')
        if self.request.method in safe:
            permission_classes = [AllowAny]
        elif self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        elif self.request.method in author_methods:
            permission_classes = [IsAuthor]
        else:
            permission_classes = [IsAdminUser]
        breakpoint()
        return [permission() for permission in permission_classes]


class AuthorViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class FeaturedBooksListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(featured=True)
        return queryset


class TrackerViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer