from django.shortcuts import render
# Create your views here.
from rest_framework import generics, status # Generic API views for specific use cases. Status class for tailoring HTTP responses. 
from rest_framework.response import Response # Django REST response hanlder tailor-made for JSON (and XML if you like)
from rest_framework.views import APIView # Wonderful generic catch-all Django REST view
from vhs_library.models import Movie, Actor, Director, Studio, Genre # Django models (python classes) that interface with our Postgres database.

from vhs_library.serializers import MovieSerializer


class MovieUpdate(APIView):

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
