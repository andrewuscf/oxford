from django.conf.urls import url, include, patterns
from rest_framework import routers
from job.api import views

router = routers.DefaultRouter()
router.register(r'place', views.PlaceViewSet)
router.register(r'worker', views.WorkerViewSet)
router.register(r'job', views.JobPositionViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls))
)