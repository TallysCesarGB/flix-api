from django.urls import path
from .views import (
    GenreListCreateAPIView,
    GenreRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path(
        '',
        GenreListCreateAPIView.as_view(),
        name='genre-list-create'
    ),
    path(
        '<int:pk>/',
        GenreRetrieveUpdateDestroyAPIView.as_view(),
        name='genre-detail'
    ),
]