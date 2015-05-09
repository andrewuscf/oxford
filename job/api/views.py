from rest_framework import viewsets, filters
from job.api.serializers import PlaceSerializer, WorkerSerializer, JobPositionSerializer, CompaniesSerializer
from job.models import Place, Worker, JobPosition, HealthCareCompany


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user',)


class JobPositionViewSet(viewsets.ModelViewSet):
    serializer_class = JobPositionSerializer
    queryset = JobPosition.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class CompaniesViewSet(viewsets.ModelViewSet):
    serializer_class = CompaniesSerializer
    queryset = HealthCareCompany.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'city', 'zipcode')
    # paginate_by = 30