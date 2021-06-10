from rest_framework import serializers

# model
from zeus.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #should not be editable
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    #create 
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)    