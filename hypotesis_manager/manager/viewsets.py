from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from django.utils import timezone

from .models import UserManager, Role, Permission, PermissionRole, Context, Country, Province, State, Language
from .serializer import UserManagerSerializer, RoleSerializer, PermissionSerializer, PermissionRoleSerializer, \
    ContextSerializer, CountrySerializer, ProvinceSerializer, StateSerializer, LanguageSerializer


def create_generic(serializer):
    if serializer.is_valid():
        object_serializer = serializer.save()
        return Response({
            'success': True,
            'data': model_to_dict(object_serializer)
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# User Manager ViewSet.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserManager.objects.all()
    serializer_class = UserManagerSerializer

    # Create.
    def create(self, request):
        serializer = UserManagerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            object_serializer = serializer.save()
            return Response({
                'success': True,
                'data': {
                    'username': object_serializer.username
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


# Context ViewSet.
class ContextViewSet(viewsets.ModelViewSet):
    queryset = Context.objects.all()
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Context.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# Country ViewSet.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    # Create.
    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Country.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.original_name = data['original_name'] if 'original_name' in data \
                else object_model.original_name
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# Province ViewSet.
class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    # Create.
    def create(self, request):
        serializer = ProvinceSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Province.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.country_id = data['country_id'] if 'country_id' in data else object_model.country_id
            object_model.original_name = data['original_name'] if 'original_name' in data \
                else object_model.original_name
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# State ViewSet.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    # Create.
    def create(self, request):
        serializer = StateSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = State.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.description = data['description'] if 'description' in data else object_model.description
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# Language ViewSet.
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    # Create.
    def create(self, request):
        serializer = LanguageSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Language.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# Role ViewSet.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        queryset = UserManager.objects.filter(role=pk)
        serializer = UserManagerSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create.
    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Role.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.is_visible = data['is_visible'] if 'is_visible' in data else object_model.is_visible
            object_model.visible_at = timezone.now() if 'is_visible' in data else object_model.visible_at
            object_model.icon = data['icon'] if 'icon' in data else object_model.icon
            object_model.description = data['description'] if 'description' in data else object_model.description
            object_model.state_id = data['state_id'] if 'state_id' in data else object_model.state_id
            object_model.state_at = timezone.now() if 'state_id' in data else object_model.state_at
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# Permission ViewSet.
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    # Create.
    def create(self, request):
        serializer = PermissionSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Permission.objects.get(pk=pk)
            object_model.is_visible = data['is_visible'] if 'is_visible' in data else object_model.is_visible
            object_model.visible_at = timezone.now() if 'is_visible' in data else object_model.visible_at
            object_model.context_id = data['context_id'] if 'context_id' in data else object_model.context_id
            object_model.description = data['description'] if 'description' in data else object_model.description
            object_model.state_id = data['state_id'] if 'state_id' in data else object_model.state_id
            object_model.state_at = timezone.now() if 'state_id' in data else object_model.state_at
            object_model.save()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


# PermissionRole ViewSet.
class PermissionRoleViewSet(viewsets.ModelViewSet):
    queryset = PermissionRole.objects.all()
    serializer_class = PermissionRoleSerializer

    # Create.
    def create(self, request):
        serializer = PermissionRoleSerializer(data=request.data)
        return create_generic(serializer)

    # Delete.
    def destroy(self, request, pk=None):
        try:
            data = request.data
            object_model = PermissionRole.objects.get(pk=pk)
            object_model.delete()
            return Response({
                'success': True,
                'data': model_to_dict(object_model)
            }, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

