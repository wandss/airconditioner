from django.urls import path

from .views import (ControlProfileListAPIView, ControlProfileRetrieveAPIView,
         ControlAPIView
        )

urlpatterns = [
        path('profiles/', ControlProfileListAPIView.as_view(), 
            name='get_profiles'),
        path('profiles/<id>', ControlProfileRetrieveAPIView.as_view(),
            name='get_profile'),
        path('', ControlAPIView.as_view(), name='control'),
    ]