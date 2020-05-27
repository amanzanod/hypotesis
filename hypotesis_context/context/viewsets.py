#from rest_framework import viewsets
#from rest_framework.exceptions import NotFound
#from django.utils.translation import gettext_lazy as _
#from django.http import QueryDict
#from rest_framework import status
#from rest_framework.response import Response
#
#from .models import Context, ContextType, Category, Format, State, Level, Language
#from .serializer import ContextSerializer, ContextTypeSerializer, CategorySerializer, FormatSerializer, \
#    StateSerializer, LevelSerializer, LanguageSerializer
#
#
## Get Context Type Id.
#def get_context_type(type_name):
#    types = ContextType.objects.filter(alias=type_name)
#    return None if types.first() is None else types.first()
#
#
## Get Context.
#def get_context(type_instance):
#    return Context.objects.none() if type_instance is None else Context.objects.filter(type_id=type_instance.id)
#
#
## ContextAbstract
#class ContextAbstractViewSet(viewsets.ModelViewSet):
#
#    context_type = None
#
#    # Perfom Create.
#    def perform_create(self, serializer: LevelSerializer):
#        if self.context_type is None:
#            try:
#                serializer.save()
#            except Exception as e:
#                raise NotFound(_("The context does not exist."))
#        else:
#            instance = serializer.instance
#            serializer.save(type=self.context_type)
#
#
## Platform ViewSet.
#class PlatformViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('platform')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## Institution ViewSet.
#class InstitutionViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('institution')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## School ViewSet.
#class SchoolViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('school')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## Grade ViewSet.
#class GradeViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('grade')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## Master ViewSet.
#class MasterViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('master')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
#class CourseViewSet(viewsets.ModelViewSet):
#    context_type = get_context_type('course')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## ClassroomViewSet ViewSet.
#class ClassroomViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('classroom')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## Course ViewSet.
#class SectionViewSet(ContextAbstractViewSet):
#    context_type = get_context_type('section')
#    queryset = get_context(context_type)
#    serializer_class = ContextSerializer
#
#
## ContextType ViewSet.
#class ContextTypeViewSet(viewsets.ModelViewSet):
#    queryset = ContextType.objects.all()
#    serializer_class = ContextTypeSerializer
#
#
## Format ViewSet.
#class FormatViewSet(viewsets.ModelViewSet):
#    queryset = Format.objects.all()
#    serializer_class = FormatSerializer
#
#
## State ViewSet.
#class StateViewSet(viewsets.ModelViewSet):
#    queryset = State.objects.all()
#    serializer_class = StateSerializer
#
#
## Level ViewSet.
#class LevelViewSet(viewsets.ModelViewSet):
#    queryset = Level.objects.all()
#    serializer_class = LevelSerializer
#
#
## Language ViewSet.
#class LanguageViewSet(viewsets.ModelViewSet):
#    queryset = Language.objects.all()
#    serializer_class = LanguageSerializer
#
#
## Category ViewSet.
#class CategoryViewSet(viewsets.ModelViewSet):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#