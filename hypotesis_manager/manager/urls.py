from django.urls import path

from rest_framework import routers

from .viewsets import UserViewSet, RoleViewSet, PermissionViewSet, PermissionRoleViewSet, ContextViewSet

route = routers.SimpleRouter()
route.register('user', UserViewSet)
route.register('context', ContextViewSet)
route.register('role', RoleViewSet)
route.register('permission', PermissionViewSet)
route.register('permissionrole', PermissionRoleViewSet)

urlpatterns = route.urls
