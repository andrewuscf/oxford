from rest_framework import serializers
from job.models import Place, Worker, JobPosition, HealthCareCompany


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('title', 'location')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCareCompany