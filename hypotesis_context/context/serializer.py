#from rest_framework import serializers
#
#from .models import Context, ContextType, Category, Format, State, Level, Language
#
#
## ContextType Serializer.
#class ContextTypeSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = ContextType
#        fields = ('id', 'name', 'alias', 'description')
#
#
## Format Serializer.
#class FormatSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Format
#        fields = ('id', 'name', 'alias', 'description')
#
#
## State Serializer.
#class StateSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = State
#        fields = ('id', 'name', 'alias', 'description')
#
#
## Level Serializer.
#class LevelSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Level
#        fields = ('id', 'name', 'alias', 'description')
#
#
## Language Serializer.
#class LanguageSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Language
#        fields = ('id', 'name', 'alias', 'description')
#
#
## Category Serializer.
#class CategorySerializer(serializers.ModelSerializer):
#    context_type = serializers.StringRelatedField(many=False)
#    parent = serializers.StringRelatedField(many=False)
#    state = serializers.StringRelatedField(many=False)
#
#    # Meta.
#    class Meta:
#        model = Category
#        fields = ('id', 'name', 'alias', 'state', 'description', 'is_visible', 'context_type',
#                  'parent', 'created_at', 'updated_at')
#        extra_kwargs = {
#            'created_at': {'read_only': True},
#            'updated_at': {'read_only': True},
#        }
#
#
## Context Serializer.
#class ContextSerializer(serializers.ModelSerializer):
#    type = ContextTypeSerializer(many=False)
#    category = CategorySerializer(many=False)
#    format = FormatSerializer(many=False)
#    state = StateSerializer(many=False)
#    level = LevelSerializer(many=False)
#    language = LanguageSerializer(many=False)
#
#    # Meta.
#    class Meta:
#        model = Context
#        fields = (
#            'id', 'type',  'name', 'alias', 'format', 'state', 'description', 'picture', 'syllabus', 'requeriments',
#            'level', 'duration', 'language', 'tech_tags', 'start_at', 'end_at', 'parent', 'teacher_main', 'category',
#            'created_at', 'updated_at')
#        extra_kwargs = {
#            'created_at': {'read_only': True},
#            'updated_at': {'read_only': True},
#            'type': {'read_only': True},
#        }
#