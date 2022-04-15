from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ControlProfile
from .serializers import ControlProfileSerializer

import subprocess


class ControlProfileListAPIView(ListAPIView):

    queryset = ControlProfile.objects.all()
    serializer_class = ControlProfileSerializer


class ControlProfileRetrieveAPIView(RetrieveAPIView):
    queryset = ControlProfile.objects.all()
    serializer_class = ControlProfileSerializer
    lookup_field = 'id'


class ControlAPIView(APIView):

    def put(self, request):

        control_data = get_object_or_404(ControlProfile, 
                id=request.data.get('id'))
        command = f"irsend,SEND_ONCE,samsung,{control_data.__str__()}"
        print(command)
        try:
            process_output = subprocess.run(command.split(','), stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, text=True)
            stdout, stderr = process_output.communicate()
            response_data = stdout
            status_code = status.HTTP_204_NO_CONTENT
        except Exception as e:
            response_data = str(e)
            status_code = status.HTTP_501_NOT_IMPLEMENTED

        return Response(data=response_data, status=status_code)


        #if control_data_id is None:
        #    response_data = 'Request data not sent or has invalid properties'
        #    status_code = status.HTTP_400_BAD_REQUEST


        #active_profile = ControlProfile.objects.filter(is_active=True)

        #if control_data:
        #    ControlProfile.objects.filter(is_active=True).update(is_active=False)
        #    response_data = None
        #    status_code = status.HTTP_204_NO_CONTENT
        #    ControlProfiles.objects.filter(id=control_data_id).update(**request.data)

        #   # control_data.is_active= True
        #   # control_date.save()
        #    

        #    if active_profile:
        #      active_profile['is_active'] = False
        #      active_profile.save()



        



        


# subprocess.run('irsend SEND_ONCE samsung on')
# process_output = subprocess.run(['date', '%a'], stdout=subprocess.PIPE,
# stderr=subprocess.PIPE, text=True)
# stdout, stderr = process_output.communicate()
# print(process_output.__dict__)
# process_output = subprocess.run(['date', '+%a'], capture_output=True)
# process_output = subprocess.run(['date', '+%a'], capture_output=True, text=True)
# print(process_output.stdout)

# >>> process_output = subprocess.run(['date', '+%a'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
# >>> process_output = subprocess.run(['date', '%a'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
