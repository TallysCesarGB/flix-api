from django.contrib import admin
from django.urls import path
from genres.views import (
    GenreListCreateAPIView,
    GenreRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # include the genres app urls
    path(
        'api/v1/genres/',
        GenreListCreateAPIView.as_view(),
        name='genre-list-create'
    ),
    path(
        'api/v1/genres/<int:pk>/',
        GenreRetrieveUpdateDestroyAPIView.as_view(),
        name='genre-detail'
        ),
]
