# Generated by Django 2.2.5 on 2020-02-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptid', models.IntegerField(verbose_name='deptid')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('no_of_students', models.IntegerField(verbose_name='no_of_studs')),
            ],
        ),
    ]
