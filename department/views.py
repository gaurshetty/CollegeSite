from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serialization import DepartmetnSer

class DepartmentOp(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmetnSer
