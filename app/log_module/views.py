from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from .filters import LogFilter
from .models import Log
from .paginators import CustomLogPaginator
from .serializers import LogCreateSerializer, LogListSerializer
from .utils import process_file_from_url


# Create your views here.

class LogView(ModelViewSet):
    queryset = Log.objects.all()
    pagination_class = CustomLogPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LogFilter
    ordering_fields = '__all__'

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return LogCreateSerializer
            case _:
                return LogListSerializer


    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'file_url': openapi.Schema(
                description='Ссылка на скачивание файла с логами',
                type=openapi.TYPE_STRING)}))
    def create(self, request, *args, **kwargs):
        errors = process_file_from_url(request.data.get('file_url'))
        if errors:
            return Response({'status': 'error', 'errors': errors}, status=400)
        return Response({'status': 'success', 'details': 'logs_uploaded'}, status=201)
