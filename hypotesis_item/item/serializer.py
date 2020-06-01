from rest_framework import serializers

from .models import Item, ItemType, Section, Format, State, Level, Language


# ItemType Serializer.
class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ('name', 'alias', 'description', 'type')


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


# Section Serializer.
class SectionSerializer(serializers.ModelSerializer):

    # Meta.
    class Meta:
        model = Section
        fields = ('id', 'name', 'alias', 'description', 'is_visible', 'course', 'order', 'picture')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Item Serializer.
class ItemSerializer(serializers.ModelSerializer):
    type = ItemTypeSerializer(many=False, read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 queryset=ItemType.objects.all(), source='type')
    format = FormatSerializer(many=False, read_only=True)
    format_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                   queryset=Format.objects.all(), source='format', required=False)
    section = SectionSerializer(many=False, read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    queryset=Section.objects.all(), source='section', required=False)
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=State.objects.all(), source='state')
    level = LevelSerializer(many=False, read_only=True)
    level_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Level.objects.all(), source='level'
                                                  , required=False)
    language = LanguageSerializer(many=False, read_only=True)
    language_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                     queryset=Language.objects.all(), source='language')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    # Meta.
    class Meta:
        model = Item
        fields = (
            'type', 'type_id', 'name', 'alias', 'format', 'state', 'description', 'picture', 'order',
            'level', 'duration', 'language', 'tech_tags', 'start_at', 'end_at',
            'created_at', 'updated_at', 'state_id', 'format_id', 'level_id', 'language_id', 'section', 'section_id')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
