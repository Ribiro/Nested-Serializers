from django.urls import path
from .views import *

urlpatterns = [
    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view()),
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view())
]
