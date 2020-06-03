from django.urls import path

from rest_framework import routers

from .viewsets import UserViewSet, RoleViewSet, PermissionViewSet, PermissionRoleViewSet, ContextViewSet, \
    CountryViewSet, ProvinceViewSet, StateViewSet, LanguageViewSet, LoginViewSet

route = routers.DefaultRouter()
route.register(r'user', UserViewSet)
route.register(r'context', ContextViewSet)
route.register(r'role', RoleViewSet)
route.register(r'permission', PermissionViewSet)
route.register(r'permissionrole', PermissionRoleViewSet)
route.register(r'country', CountryViewSet)
route.register(r'province', ProvinceViewSet)
route.register(r'state', StateViewSet)
route.register(r'language', LanguageViewSet)
route.register(r'login', LoginViewSet)

urlpatterns = route.urls
