from django.conf.urls import url, include, patterns
from rest_framework import routers
from job.api import views

router = routers.DefaultRouter()
router.register(r'places', views.PlaceViewSet)
router.register(r'workers', views.WorkerViewSet)
router.register(r'jobs', views.JobPositionViewSet)
router.register(r'companies', views.CompaniesViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls))
)