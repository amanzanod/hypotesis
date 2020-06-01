from django.urls import path

from rest_framework import routers

from .viewsets import ItemTypeViewSet, SectionViewSet, FormatViewSet, StateViewSet, \
    LevelViewSet, LanguageViewSet, ItemViewSet

route = routers.SimpleRouter()
route.register('item', ItemViewSet)
route.register('item_type', ItemTypeViewSet)
route.register('section', SectionViewSet)
route.register('format', FormatViewSet)
route.register('state', StateViewSet)
route.register('level', LevelViewSet)
route.register('language', LanguageViewSet)

urlpatterns = route.urls
