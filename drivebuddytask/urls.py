from django.conf.urls import url, include
from rest_framework import routers
from drivers import views

router = routers.DefaultRouter()
router.register(r'drivers', views.DriverViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
