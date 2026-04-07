from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from core.permissions import GlobalDefultPermissionClass


class ReviewListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefultPermissionClass)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
