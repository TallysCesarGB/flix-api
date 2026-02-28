from django.urls import path
from . import views
from .views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(
        'autocomplete/nationality/',
        views.nationality_autocomplete,
        name='nationality-autocomplete'
        ),
    path(
        '',
        ActorListCreateAPIView.as_view(),
        name='actor-list-create'
        ),
    path(
        '<int:pk>/',
        ActorRetrieveUpdateDestroyAPIView.as_view(),
        name='actor-detail'
        ),
]