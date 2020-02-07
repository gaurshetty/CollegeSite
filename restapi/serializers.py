from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Student


class StudentSer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
