from django.urls import path

from measurement.views import SensorAPIView, SensorAPIUpdate, MeasurementAPIView, SensorRetrieveAPIView

urlpatterns = [
    path('sensors/', SensorAPIView.as_view()),
    path('sensors/<int:pk>/', SensorAPIUpdate.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveAPIView.as_view()),
]
