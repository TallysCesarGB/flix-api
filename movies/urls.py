from django.urls import path
from .views import (
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    MovieStatsAPIView
)


urlpatterns = [
    path(
        '',
        MovieListCreateAPIView.as_view(),
        name='movie-list-create'
        ),
    path(
        '<int:pk>/',
        MovieRetrieveUpdateDestroyAPIView.as_view(),
        name='movie-detail'
        ),
    path(
        'stats/',
        MovieStatsAPIView.as_view(),
        name='movie-stats'
        ),
]