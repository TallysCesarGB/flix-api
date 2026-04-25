from rest_framework import serializers
import datetime
from django.db.models import Avg
from .models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        ratings = obj.reviews.all()
        if ratings.exists():
            return round(ratings.aggregate(average=Avg('rating'))['average'], 1)
        return None

    def validate_release_date(self, value):
        if value and (value < datetime.data(1888, 1, 1) or value > datetime.date.today()):
            return serializers.ValidationError("Release date must be between January 1, 1888 and today.")
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genre = GenreSerializer(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'release_date',
            'genre',
            'actors',
            'rate'
        ]

    def get_rate(self, obj):
        ratings = obj.reviews.all()
        if ratings.exists():
            return round(ratings.aggregate(average=Avg('rating'))['average'], 1)
        return 0
