from django.db import models

class Department(models.Model):
    deptid = models.IntegerField("deptid")
    name   = models.CharField("name",max_length=50)
    no_of_students = models.IntegerField("no_of_studs")
