from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.utils import timezone

from .models import Context, ContextType, Category, Format, State, Level, Language
from .serializer import ContextSerializer, ContextTypeSerializer, CategorySerializer, FormatSerializer, \
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
def update_context(data, pk):
    try:
        object_model = Context.objects.get(pk=pk)
        object_model.name = data['name'] if 'name' in data else object_model.name
        object_model.type_id = data['type_id'] if 'type_id' in data else object_model.type_id
        object_model.format_id = data['format_id'] if 'format_id' in data else object_model.format_id
        object_model.state_id = data['state_id'] if 'state_id' in data else object_model.state_id
        object_model.state_at = timezone.now() if 'state_id' in data else object_model.state_at
        object_model.description = data['description'] if 'description' in data else object_model.description
        object_model.syllabus = data['syllabus'] if 'syllabus' in data else object_model.syllabus
        object_model.requeriments = data['requeriments'] if 'requeriments' in data else object_model.requeriments
        object_model.level_id = data['level_id'] if 'level_id' in data else object_model.level_id
        object_model.duration = data['duration'] if 'duration' in data else object_model.duration
        object_model.language_id = data['language_id'] if 'language_id' in data else object_model.language_id
        object_model.level_id = data['level_id'] if 'level_id' in data else object_model.level_id
        object_model.tech_tags = data['tech_tags'] if 'tech_tags' in data else object_model.tech_tags
        object_model.parent_id = data['parent_id'] if 'parent_id' in data else object_model.parent_id
        object_model.teacher_main = data['teacher_main'] if 'teacher_main' in data else object_model.teacher_main
        object_model.category_id = data['category_id'] if 'category_id' in data else object_model.category_id
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


# ContextAbstract
class ContextAbstractViewSet(viewsets.ModelViewSet):
    context_type = None

    # Perfom Create.
    def perform_create(self, serializer: LevelSerializer):
        if self.context_type is None:
            try:
                serializer.save()
            except Exception as e:
                raise NotFound(_("The context does not exist."))
        else:
            instance = serializer.instance
            serializer.save(type=self.context_type)


# Platform ViewSet.
class PlatformViewSet(ContextAbstractViewSet):
    queryset = Context.objects.filter(type='platform')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


# Institution ViewSet.
class InstitutionViewSet(ContextAbstractViewSet):
    queryset = Context.objects.filter(type='institution')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


# School ViewSet.
class SchoolViewSet(ContextAbstractViewSet):
    queryset = Context.objects.filter(type='school')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


# Grade ViewSet.
class GradeViewSet(ContextAbstractViewSet):
    queryset = Context.objects.filter(type='grade')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


# Master ViewSet.
class MasterViewSet(ContextAbstractViewSet):
    queryset = Context.objects.filter(type='master')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Context.objects.filter(type='course')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


# ClassroomViewSet ViewSet.
class ClassroomViewSet(ContextAbstractViewSet):
    queryset = Context.objects.filter(type='classroom')
    serializer_class = ContextSerializer

    # Create.
    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        return create_context(serializer)

    # Create.
    def update(self, request, pk=None):
        data = request.data
        return update_context(data, pk)


# ContextType ViewSet.
class ContextTypeViewSet(viewsets.ModelViewSet):
    queryset = ContextType.objects.all()
    serializer_class = ContextTypeSerializer

    # Create.
    def create(self, request):
        serializer = ContextTypeSerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = ContextType.objects.get(pk=pk)
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


# Category ViewSet.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Create.
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        return create_generic(serializer)

    # Update.
    def update(self, request, pk=None):
        try:
            data = request.data
            object_model = Category.objects.get(pk=pk)
            object_model.name = data['name'] if 'name' in data else object_model.alias
            object_model.state_id = data['state_id'] if 'state_id' in data else object_model.state_id
            object_model.state_at = timezone.now() if 'state_id' in data else object_model.state_at
            object_model.is_visible = data['is_visible'] if 'is_visible' in data else object_model.is_visible
            object_model.visible_at = timezone.now() if 'is_visible' in data else object_model.visible_at
            object_model.description = data['description'] if 'description' in data else object_model.description
            object_model.context_type_id = data['context_type_id'] \
                if 'context_type_id' in data else object_model.context_type_id
            object_model.parent_id = data['parent_id'] if 'parent_id' in data else object_model.parent_id
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
