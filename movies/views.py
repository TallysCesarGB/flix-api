from django.db.models import Count, Avg
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import views, response, status
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from reviews.models import Review
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


class MovieStatsAPIView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Movie.objects.all()
    
    def get(self, request):
        total_movies = self.queryset.count()
        movies_per_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_rating = Review.objects.aggregate(average_rating=Avg('rating'))['average_rating']
        
        return response.Response(
            data={
                'total_movies':total_movies,
                'movies_per_genre': movies_per_genre,
                'total_reviews': total_reviews,
                'average_rating': round(average_rating, 2) if average_rating is not None else 0
            },
            status=status.HTTP_200_OK
        )