import requests
from django.http import JsonResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from .models import Actor
from .serializers import ActorSerializer


def nationality_autocomplete(request):
    query = request.GET.get('q', '').lower().strip()
    response = requests.get('https://restcountries.com/v3.1/all?fields=demonyms')
    countries = response.json()
    
    suggestions = []
    for country in countries:
        nation = country.get('demonyms', {}).get('eng', {}).get('m', '')
        if nation and query in nation.lower():
            suggestions.append(nation)
    
    return JsonResponse({'results': sorted(set(suggestions))[:10]})


class ActorListCreateAPIView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer