from rest_framework import serializers
from rest_framework.response import Response

from .models import UserManager, Role, Permission, PermissionRole, Context, Province, Country, State, Language


# Context Serializer.
class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = ('alias', 'name')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Country Serializer.
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('code', 'name', 'original_name')


# Province Serializer.
class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False, read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    queryset=Country.objects.all(), source='country')

    class Meta:
        model = Province
        fields = ('code', 'name', 'original_name', 'country', 'country_id')


# State Serializer.
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('alias', 'name', 'description')


# Language Serializer.
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code', 'name', 'description')


# Permission Serializer.
class PermissionSerializer(serializers.ModelSerializer):
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=State.objects.all(), source='state')
    context = ContextSerializer(many=False, read_only=True)
    context_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    queryset=Context.objects.all(), source='context')

    class Meta:
        model = Permission
        fields = ('alias', 'state', 'state_id', 'is_visible', 'description', 'context', 'context_id',
                  'created_at', 'updated_at', 'roles')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Role Serializer.
class RoleSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=State.objects.all(), source='state')

    class Meta:
        model = Role
        fields = ('alias', 'name', 'state', 'state_id', 'is_visible', 'icon', 'description',
                  'created_at', 'updated_at', 'permissions')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'permissions': {'read_only': True},
        }


# PermissionRole Serializer.
class PermissionRoleSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=False, read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Role.objects.all(), source='role')

    permission = PermissionSerializer(many=False, read_only=True)
    permission_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                       queryset=Permission.objects.all(), source='permission')


    class Meta:
        model = PermissionRole
        fields = ('id', 'role', 'role_id', 'permission', 'permission_id', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# User Serializer.
class UserManagerSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=False, read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Role.objects.all(), source='role')
    province = ProvinceSerializer(many=False, read_only=True)
    province_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                     queryset=Province.objects.all(), source='province')
    country = CountrySerializer(many=False, read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                     queryset=Country.objects.all(), source='country')
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  queryset=State.objects.all(), source='state')
    language = LanguageSerializer(many=False, read_only=True)
    language_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                     queryset=Language.objects.all(), source='language')
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    picture = serializers.ImageField(allow_empty_file=True)

    class Meta:
        model = UserManager
        fields = (
            'username', 'password', 'is_visible', 'state', 'state_id', 'picture', 'name', 'surname1', 'surname2',
            'title', 'email', 'city', 'province', 'province_id', 'country', 'country_id', 'address', 'postal_code',
            'language', 'language_id', 'about_me', 'role', 'role_id', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'state': {'read_only': True},
        }

