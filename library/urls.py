"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from api import views

router = routers.SimpleRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)

books_router = routers.NestedSimpleRouter(router, 'books', lookup='book')
books_router.register('reviews', views.ReviewViewSet, basename='book-reviews')
books_router.register('tracker', views.TrackerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
    path('', include(books_router.urls)),
    path('featured/', views.FeaturedBooksListView.as_view(), name='featured_books')
]
