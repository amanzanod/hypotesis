from django.urls import path

from rest_framework import routers

from .viewsets import CourseViewSet,  ContextTypeViewSet, CategoryViewSet, FormatViewSet, \
    StateViewSet, LevelViewSet, LanguageViewSet, InstitutionViewSet, PlatformViewSet, SchoolViewSet, GradeViewSet, \
    MasterViewSet, ClassroomViewSet

route = routers.SimpleRouter()
route.register('platform', PlatformViewSet)
route.register('institution', InstitutionViewSet)
route.register('school', SchoolViewSet)
route.register('grade', GradeViewSet)
route.register('master', MasterViewSet)
route.register('course', CourseViewSet)
route.register('classroom', ClassroomViewSet)
route.register('context_type', ContextTypeViewSet)
route.register('category', CategoryViewSet)
route.register('format', FormatViewSet)
route.register('state', StateViewSet)
route.register('level', LevelViewSet)
route.register('language', LanguageViewSet)

urlpatterns = route.urls
