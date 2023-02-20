from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    appointment_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    department_id = models.IntegerField(3, null=True)
    created_by = models.IntegerField(3, null=True)
    deleted_by = models.IntegerField(3, null=True)