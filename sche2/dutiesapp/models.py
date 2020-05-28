from django.db import models

# Create your models here.
from django.db import models
class teacher(models.Model):
    initials=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    n_duties=models.IntegerField(default=0)
    n_dutiesassigned=models.IntegerField(default=0)

    n_am=models.IntegerField(default=0)
    n_pm=models.IntegerField(default=0)
    n_relief=models.IntegerField(default=0)
    n_dates=models.CharField(max_length=500,default='')
    leaves=models.CharField(max_length=1000,default='')
    Flag=models.IntegerField(default=0)

class exam(models.Model):
    date=models.CharField(max_length=50)
    n_students=models.IntegerField(default=0)
    n_rooms=models.IntegerField(default=0)
    n_acs=models.IntegerField(default=0)
    n_ds=models.IntegerField(default=0)
    n_rs=models.IntegerField(default=0)
    n_relief=models.IntegerField(default=0)
    acs=models.CharField(max_length=500)
    ds = models.CharField(max_length=500)
    rs = models.CharField(max_length=500)
    relief = models.CharField(max_length=500)
