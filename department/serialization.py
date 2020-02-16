from rest_framework.serializers import ModelSerializer
from .models import *

class DepartmetnSer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'