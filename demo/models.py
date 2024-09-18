from django.db import models
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your models here.
class Income(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    description = models.CharField(max_length=80)

class Expense(models.Model):
    ename = models.CharField(max_length=30)
    eamount = models.IntegerField()
    edescription = models.CharField(max_length=80)
