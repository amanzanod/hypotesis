from rest_framework import serializers

from .models import Context, ContextType, Category, Format, State, Level, Language


# ContextType Serializer.
class ContextTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextType
        fields = ('name', 'alias', 'description')


# Format Serializer.
class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ('name', 'alias', 'description')


# State Serializer.
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'alias', 'description')


# Level Serializer.
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('name', 'alias', 'description')


# Language Serializer.
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code', 'name', 'description')


# Category Serializer.
class CategorySerializer(serializers.ModelSerializer):
    context_type = ContextTypeSerializer(many=False, read_only=True)
    context_type_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                         queryset=ContextType.objects.all(), source='context_type')
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', required=False)
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=State.objects.all(), source='state')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    # Meta.
    class Meta:
        model = Category
        fields = ('name', 'alias', 'state', 'description', 'is_visible', 'context_type', 'context_type_id', 'state_id',
                  'parent', 'created_at', 'updated_at', 'parent_id')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Context Serializer.
class ContextSerializer(serializers.ModelSerializer):
    type = ContextTypeSerializer(many=False, read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=ContextType.objects.all(), source='type')
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, required=False,
                                                     queryset=Category.objects.all(), source='category')
    format = FormatSerializer(many=False, read_only=True)
    format_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                   queryset=Format.objects.all(), source='format', required=False)
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=State.objects.all(), source='state')
    level = LevelSerializer(many=False, read_only=True)
    level_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Level.objects.all(), source='level'
                                                  , required=False)
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Context.objects.all(), source='context', required=False)
    language = LanguageSerializer(many=False, read_only=True)
    language_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                     queryset=Language.objects.all(), source='language')

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    start_at = serializers.DateTimeField(format="%Y-%m-%d ", read_only=True)
    end_at = serializers.DateTimeField(format="%Y-%m-%d ", read_only=True)

    # Meta.
    class Meta:
        model = Context
        fields = (
            'type', 'type_id', 'name', 'alias', 'format', 'state', 'description', 'picture', 'syllabus', 'requeriments',
            'level', 'duration', 'language', 'tech_tags', 'start_at', 'end_at', 'parent', 'teacher_main', 'category',
            'created_at', 'updated_at', 'state_id', 'category_id', 'format_id', 'level_id', 'language_id', 'parent_id')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
