from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.SET_NULL, null=True)
    utype = models.IntegerField(null=True)

class Medicine(models.Model):
    mid = models.AutoField
    mname = models.CharField(max_length=50)
    minfo = models.CharField(max_length=50, default="",null=True)
    mprice = models.IntegerField(default=0,null=True)
    mqty = models.IntegerField(default=0,null=True)
    def __str__(self):
        return self.mname

class Order(models.Model):
    oid = models.AutoField
    status = models.IntegerField(default=2,null=True)
    lastComment = models.CharField(max_length=100,null=True)
    lastAcess = models.DateTimeField(default=datetime.now, blank=True)
    total = models.IntegerField(default=0,null=True)

class orderDetail(models.Model):
    ooid = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, related_name='order_id')
    omid = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, null=True, related_name='omid')
    omqty = models.IntegerField(default=0, null=True)

class Consumption(models.Model):
    cid = models.AutoField
    patientID = models.CharField(max_length=100,null=True)
    desc = models.CharField(max_length=100,null=True)
    dateIssued = models.DateTimeField(default=datetime.now, blank=True)

class consumptionDetail(models.Model):
    ccid = models.ForeignKey(
        Consumption, on_delete=models.CASCADE, null=True, related_name='comsumption_id')
    cmid = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, null=True, related_name='cmid')
    cmqty = models.IntegerField(default=0, null=True)
