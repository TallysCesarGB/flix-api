from rest_framework import serializers
import datetime
from django.db.models import Avg
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        ratings = obj.reviews.all()
        if ratings.exists():
            return round(ratings.aggregate(average=Avg('rating'))['rating__avg'], 1)
        return None

    def validate_release_date(self, value):
        if value and value < '1888-01-01' or value > datetime.date.today():
            return serializers.ValidationError("Release date must be between January 1, 1888 and today.")
        return value
