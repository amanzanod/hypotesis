from rest_framework import serializers

from .models import State, EnrolContext


# State Serializer.
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'alias', 'description')


# EnrolContext Serializer.
class EnrolContextSerializer(serializers.ModelSerializer):
    state = StateSerializer(many=False, read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=State.objects.all(), source='state')

    # Meta.
    class Meta:
        model = EnrolContext
        fields = ('id', 'user', 'context', 'role', 'state', 'state_id', 'state_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
