from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from django.db.models import Count

from manabiyacentral.middlewares.parsers import RequestParser

from .models import (
    Statements,
    WodaDocs
)

from .sanitizers import Sanitize

from .serializers import (
    StatementsSerializer,
    WodaDocSerializer,
    WodaFolderCountSerializer,
    StatementFolderCountSerializer,
    StatementFileSerializer,
    WodaFileSerializer
    )


class StatementView(viewsets.ModelViewSet):
    queryset = Statements.objects.all()
    serializer_class = StatementsSerializer
    parser_classes = [MultiPartParser, RequestParser]

    def create(self, request, *args, **kwargs):
        sanitized_data = Sanitize.create_statement(request=request)
        serializer = self.get_serializer(data=sanitized_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_distinct_folder(self, request, *args, **kwargs):
        folder_counts = (
            Statements.objects.values('folder_name').annotate(count=Count('id')).order_by('folder_name')
        )
        serializer = StatementFolderCountSerializer(folder_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_file_names_for_folder(self, request):
        folder_name = request.query_params.get('folder_name','')
        file_names = Statements.objects.filter(folder_name=folder_name)
        serializer = StatementFileSerializer(file_names, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WodaDocView(viewsets.ModelViewSet):
    queryset = WodaDocs.objects.all()
    serializer_class = WodaDocSerializer
    parser_classes = [MultiPartParser, RequestParser]

    def create(self, request, *args, **kwargs):
        sanitized_data = Sanitize.create_wodadoc(request=request)
        serializer = self.get_serializer(data=sanitized_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_distinct_folder(self, request, *args, **kwargs):
        folder_counts = (
            WodaDocs.objects.values('folder_name').annotate(count=Count('id')).order_by('folder_name')
        )
        serializer = WodaFolderCountSerializer(folder_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_file_names_for_folder(self, request):
        folder_name = request.query_params.get('folder_name','') 
        file_names = WodaDocs.objects.filter(folder_name=folder_name)
        serializer = WodaFileSerializer(file_names, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    