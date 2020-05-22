from rest_framework import viewsets

from .models import User, Role, Permission, PermissionRole, Context
from .serializer import UserSerializer, RoleSerializer, PermissionSerializer, PermissionRoleSerializer, \
    ContextSerializer


# User ViewSet.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Context ViewSet.
class ContextViewSet(viewsets.ModelViewSet):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer


# Role ViewSet.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# Permission ViewSet.
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


# PermissionRole ViewSet.
class PermissionRoleViewSet(viewsets.ModelViewSet):
    queryset = PermissionRole.objects.all()
    serializer_class = PermissionRoleSerializer


