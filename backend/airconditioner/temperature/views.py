from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os

class TemperatureAPIView(APIView):

    def get(self, request):
        base_dir = '/sys/bus/w1/devices/'
        device = '28-9f2edc0664ff'
        ark = 'w1_slave'

        try:
            with open(f'{base_dir}/{device}/{ark}', 'r') as raw_data:
                temperature = raw_data.read()
                temperature = float(temperature.split('=')[-1])
            response_data = {"room_temperature": temperature}
            status_code = status.HTTP_200_OK

        except Exception as e:
            response_data = str(e)
            status_code = status.HTTP_404_NOT_FOUND

        return Response(data=response_data, status=status_code)
