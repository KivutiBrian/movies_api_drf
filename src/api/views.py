from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# models
from zeus.models import Movie
# serializers
from .serializer import MovieSerializer

# a list of all movies
@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        # get all movies
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # serialize data
        serializer = MovieSerializer(data=request.data)
        # check if it valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            return Response(serializer.data)
        else:
            # return an error
            return Response(serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def movie(request, pk):
    
    a_movie = Movie.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = MovieSerializer(a_movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MovieSerializer(a_movie,data=request.data)
        # check if it valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            return Response(serializer.data)
        else:
            # return an error
            return Response(serializer.errors)


    if request.method == 'DELETE':
        a_movie.delete()
        return Response({"message":"Record Deleted"})