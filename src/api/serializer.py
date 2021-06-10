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

    # update
    def update(self, instance, validated_data): #instance carries the old values while validated_data is the new data
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance