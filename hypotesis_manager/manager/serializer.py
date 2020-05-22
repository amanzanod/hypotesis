from rest_framework import serializers

from .models import User, Role, Permission, PermissionRole, Context


# User Serializer.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'is_visible', 'state', 'picture', 'name', 'surname1', 'surname2',
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
        fields = ('id', 'alias', 'name')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Role Serializer.
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'alias', 'name', 'state', 'is_visible', 'icon', 'description', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


# Permission Serializer.
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'alias', 'state', 'is_visible', 'description', 'context', 'created_at', 'updated_at', 'roles')
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
