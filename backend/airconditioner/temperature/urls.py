from django.urls import path

from .views import TemperatureAPIView

urlpatterns = [
        path('', TemperatureAPIView.as_view(), 
            name='get_temperature')
    ]
