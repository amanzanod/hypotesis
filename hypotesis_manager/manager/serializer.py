from rest_framework import serializers
from django.utils.timesince import timesince

from .models import UserManager, Role, Permission, PermissionRole, Context


# User Serializer.
class UserManagerSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(many=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = UserManager
        fields = (
            'username', 'password', 'is_visible', 'state', 'picture', 'name', 'surname1', 'surname2',
            'title', 'email', 'city', 'province', 'country', 'address', 'postal_code', 'language', 'about_me',
            'role', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Context Serializer.
class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = ('alias', 'name')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Role Serializer.
class RoleSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Role
        fields = ('alias', 'name', 'state', 'is_visible', 'icon', 'description', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Permission Serializer.
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('alias', 'state', 'is_visible', 'description', 'context', 'created_at', 'updated_at', 'roles')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# PermissionRole Serializer.
class PermissionRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRole
        fields = ('id', 'role', 'permission', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
