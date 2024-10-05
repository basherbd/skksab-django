from django.db import models
from datetime import date


# Create your models here.
class Student(models.Model):
  month = models.CharField(max_length=50)
  saving = models.CharField(max_length=50)
  profit = models.CharField(max_length=50, null=True, blank=True)
  withdraw = models.CharField(max_length=50, null=True, blank=True)
  total = models.CharField(max_length=50)
  loan = models.CharField(max_length=50, null=True, blank=True)
  install = models.CharField(max_length=50, null=True, blank=True)
  install_no = models.IntegerField(null=True, blank=True)
  install_due = models.CharField(max_length=50, null=True, blank=True)
  date = models.CharField(max_length=50)
  """date = models.DateField(auto_now_add=False, auto_now=False, blank=True)"""
  remark = models.CharField(max_length=255)

  def __str__(self):
    return f'Student: {self.month}'
