from django.db import models


class Student(models.Model):
    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', max_length=100)
    age = models.IntegerField('age')
    gender = models.CharField('gender', max_length=10)
    fees = models.FloatField('fees')
    address = models.TextField('address', max_length=100)
    active = models.CharField('isactive', max_length=10, default='Y')
