from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serialization import DepartmetnSer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.response import Response
class DepartmentOp(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmetnSer
    permission_classes = (IsAuthenticated,)
    authentication_classes =[BasicAuthentication]

    def FElist(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(no_of_students__gte=100))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)