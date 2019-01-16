from django.shortcuts import render
from .models import test
from rest_framework import viewsets
from app_test.serialise import TestSerializer
# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = test.objects.all()
    serializer_class = TestSerializer