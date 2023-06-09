from django.shortcuts import render
from .models import Metadata, Measure, Session, Classes, Subject, Channel, TimeSerie
from .serializers import MetadataSerializer, MeasureSerializer, SessionSerializer, ClassesSerializer, SubjectSerializer, ChannelSerializer, TimeSerieGetSerializer, TimeSeriePostSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TimeSerieFilter
# Create your views here.

class MetadataView(generics.ListCreateAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class MeasureView(generics.ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

class SessionView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ClassesView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ChannelView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class TimeSerieView(generics.ListCreateAPIView):
    queryset = TimeSerie.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TimeSerieFilter
    #serializer_class = TimeSerieSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TimeSerieGetSerializer
        elif self.request.method == 'POST':
            return TimeSeriePostSerializer