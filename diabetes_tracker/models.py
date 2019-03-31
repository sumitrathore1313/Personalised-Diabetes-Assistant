from django.db import models
import datetime

# Create your models here.
class Glucose(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, null=False)
    glucose = models.IntegerField(null=False)
    sleep = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    duration_of_exercise = models.IntegerField(null=False)
    type_of_exercise = models.CharField(max_length=128)
