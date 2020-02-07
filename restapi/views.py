from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSer
from .models import Student


class StudentOperations(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
