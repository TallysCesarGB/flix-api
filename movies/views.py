from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer
from core.permissions import GlobalDefultPermissionClass

class MovieListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer