from rest_framework import serializers

from .models import ControlProfile


class ControlProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlProfile
        fields = '__all__'




