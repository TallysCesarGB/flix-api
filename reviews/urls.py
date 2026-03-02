from django.urls import path
from .views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(
        '',
        ReviewListCreateAPIView.as_view(),
        name='movie-list-create'
        ),
    path(
        '<int:pk>/',
        ReviewRetrieveUpdateDestroyAPIView.as_view(),
        name='movie-detail'
        ),
]