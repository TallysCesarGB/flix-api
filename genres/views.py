import json
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from .models import Genre
from .serializers import GenreSerializer
from rest_framework.generics import ListCreateAPIView 
import django.views.decorators.csrf as csrf


class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class GenreRetrieveUpdateDestroyAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer