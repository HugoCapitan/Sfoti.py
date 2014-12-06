from .models import Album
from .serializers import AlbumSerializer
from rest_framework import viewsets
from django.shortcuts import render


class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	model = Album