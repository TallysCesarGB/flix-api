from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from .serializers import GenreSerializer
from core.permissions import GlobalDefultPermissionClass


class GenreListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer