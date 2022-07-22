from rest_framework import serializers

from .models import ControlProfile, AirConditionerStatus


class ControlProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlProfile
        fields = '__all__'

class AirConditionerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirConditionerStatus
        fields = 'status'
