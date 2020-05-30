from django.urls import path

from rest_framework import routers

from .viewsets import UserViewSet, RoleViewSet, PermissionViewSet, PermissionRoleViewSet, ContextViewSet

route = routers.DefaultRouter()
route.register(r'user', UserViewSet)
route.register(r'context', ContextViewSet)
route.register(r'role', RoleViewSet)
route.register(r'permission', PermissionViewSet)
route.register(r'permissionrole', PermissionRoleViewSet)

urlpatterns = route.urls
