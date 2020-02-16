from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serialization import DepartmetnSer
from rest_framework.permissions import AllowAny,IsAuthenticated
class DepartmentOp(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmetnSer
    permission_classes = (AllowAny,)