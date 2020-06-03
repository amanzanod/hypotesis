from django.urls import path

from rest_framework import routers

from .viewsets import EnrolContextViewSet, StateViewSet

route = routers.SimpleRouter()
route.register('enrol', EnrolContextViewSet)
route.register('state', StateViewSet)

urlpatterns = route.urls
