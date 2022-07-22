from django.urls import path

from .views import (ControlProfileListAPIView, ControlProfileRetrieveAPIView,
         ControlAPIView, AirConditionerStatusRetrieveAPIView
        )

urlpatterns = [
        path('profiles/', ControlProfileListAPIView.as_view(), 
            name='get_profiles'),
        path('profiles/<id>', ControlProfileRetrieveAPIView.as_view(),
            name='get_profile'),
        path('status', AirConditionerStatusRetrieveAPIView.as_view(),
            name='get_status'),
        path('', ControlAPIView.as_view(), name='control'),
    ]
