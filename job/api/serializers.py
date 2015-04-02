from rest_framework import serializers
from job.models import Place, Worker, JobPosition


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'address', 'city', 'state', 'country', 'zip_code')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition