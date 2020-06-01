from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import Item, ItemType, Section, Format, State, Level, Language
from .serializer import ItemSerializer, ItemTypeSerializer, SectionSerializer, FormatSerializer, \
    StateSerializer, LevelSerializer, LanguageSerializer


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


def create_context(serializer):
    if serializer.is_valid():
        object_serializer = serializer.save()
        return Response({
            'success': True,
            'data': {
                'alias': object_serializer.alias
            }
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Update.
def update_context(data, object_model):
    try:
        object_model.name = data['name'] if 'name' in data else object_model.name
        object_model.type_id = data['type_id'] if 'type_id' in data else object_model.type_id
        object_model.format_id = data['format_id'] if 'format_id' in data else object_model.format_id
        object_model.state_id = data['state_id'] if 'state_id' in data else object_model.state_id
        object_model.is_visible = data['is_visible'] if 'is_visible' in data else object_model.is_visible
        object_model.description = data['description'] if 'description' in data else object_model.description
        object_model.level_id = data['level_id'] if 'level_id' in data else object_model.level_id
        object_model.duration = data['duration'] if 'duration' in data else object_model.duration
        object_model.language_id = data['language_id'] if 'language_id' in data else object_model.language_id
        object_model.tech_tags = data['tech_tags'] if 'tech_tags' in data else object_model.tech_tags
        object_model.section_id = data['parent_id'] if 'parent_id' in data else object_model.section_id
        object_model.picture = data['picture'] if 'picture' in data else object_model.picture
        object_model.save()
        return Response({
            'success': True,
            'data': object_model.alias
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'errors': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


# Item ViewSet.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Create.
    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        object_model = Item.objects.get(pk=pk)
        return update_context(data, object_model)


# ItemType ViewSet.
class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer

    # Create.
    def create(self, request):
        serializer = ItemTypeSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = ItemType.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.description = data['description'] if 'description' in data else object_model.description
            object_model.type = data['type'] if 'type' in data else object_model.type
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


# Format ViewSet.
class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer

    # Create.
    def create(self, request):
        serializer = FormatSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Format.objects.get(pk=pk)
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


# Level ViewSet.
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    # Create.
    def create(self, request):
        serializer = LevelSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Level.objects.get(pk=pk)
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


# Section ViewSet.
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        queryset = Item.objects.filter(section=pk)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create.
    def create(self, request):
        serializer = SectionSerializer(data=request.data)
        return create_context(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Section.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.name
            object_model.alias = data['alias'] if 'alias' in data else object_model.alias
            object_model.is_visible = data['is_visible'] if 'is_visible' in data else object_model.is_visible
            object_model.description = data['description'] if 'description' in data else object_model.description
            object_model.course = data['course'] if 'course' in data else object_model.course
            object_model.order = data['order'] if 'order' in data else object_model.order
            object_model.save()
            return Response({
                'success': True,
                'data': object_model.alias
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
