from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.utils import timezone

from .models import State, EnrolContext
from .serializer import StateSerializer, EnrolContextSerializer


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


# EnrolContext ViewSet.
class EnrolContextViewSet(viewsets.ModelViewSet):
    queryset = EnrolContext.objects.all()
    serializer_class = EnrolContextSerializer

    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        queryset = EnrolContext.objects.filter(context=pk)
        serializer = EnrolContextSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        queryset = EnrolContext.objects.filter(context=pk, role='student')
        serializer = EnrolContextSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def teachers(self, request, pk=None):
        queryset = EnrolContext.objects.filter(context=pk, role='teacherpro')
        serializer = EnrolContextSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        queryset = EnrolContext.objects.filter(user=pk)
        serializer = EnrolContextSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create.
    def create(self, request):
        serializer = EnrolContextSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = State.objects.get(pk=pk)
            object_model.user = data['user'] if 'user' in data else object_model.user
            object_model.context = data['context'] if 'context' in data else object_model.context
            object_model.role = data['role'] if 'role' in data else object_model.role
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


