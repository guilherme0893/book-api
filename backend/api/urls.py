from django.urls import path
from .views.Author import AuthorDetailView, AuthorView
from .views.Book import BookView, BookDetailView

urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('authors/<str:pk>', AuthorDetailView.as_view()),
    path('books/', BookView.as_view()),
    path('books/<str:pk>', BookDetailView.as_view()),
]
