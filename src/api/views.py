from django.db.models.base import Model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# models
from zeus.models import Movie
# serializers
from .serializer import MovieSerializer

# a list of all movies
@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        # get all movies
        try:
            movies = Movie.objects.all()
        except Exception as e:
            return Response({"Error": "Could not fetch movie list, try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # serialize data
        serializer = MovieSerializer(data=request.data)
        # check if it valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # return an error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def movie(request, pk):
    
    try:
        a_movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response({"Error": "No record matches the ID provided"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(a_movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = MovieSerializer(a_movie,data=request.data)
        # check if it valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # return an error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        a_movie.delete()
        return Response({"message":"Record Deleted"}, status=status.HTTP_200_OK)