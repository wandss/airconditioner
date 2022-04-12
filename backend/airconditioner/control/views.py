from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import ControlProfile
from .serializers import ControlProfileSerializer


class ControlProfileListAPIView(ListAPIView):

    queryset = ControlProfile.objects.all()
    serializer_class = ControlProfileSerializer


class ControlProfileRetrieveAPIView(RetrieveAPIView):
    queryset = ControlProfile.objects.all()
    serializer_class = ControlProfileSerializer
    lookup_field = 'id'





