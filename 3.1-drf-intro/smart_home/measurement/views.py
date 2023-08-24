# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer

"""Получить список датчиков"""
"""Создать датчик"""
class SensorAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


"""Изменить датчик"""
class SensorAPIUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


"""Добавить измерение"""
class MeasurementAPIView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


"""Получить информацию по конкретному датчику"""
class SensorRetrieveAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer









