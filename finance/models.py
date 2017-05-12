# -*- coding: utf-8 -*-
from django.db import models
import django.utils.timezone as timezone

class Users(models.Model):

    telephone = models.CharField(max_length=30)
    moneys = models.CharField(max_length=30)
    invitation = models.IntegerField(default=0)
    uid = models.CharField(max_length=30,default=0)
    purchase_times = models.IntegerField(default=0)
    new_awards = models.IntegerField(default=30)
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.uid


class Consumption_record(models.Model):
    uid = models.IntegerField()
    user_id = models.ForeignKey(Users)
    amount = models.CharField(max_length=30)
    group_id = models.IntegerField(default=0)
    create_at = models.DateTimeField(default=timezone.now)
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.create_at

class Recharge_record(models.Model):
    uid = models.IntegerField()
    out_no = models.CharField(max_length=30)
    user_id = models.ForeignKey(Users)
    amount = models.CharField(max_length=30)
    status = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.now)
    pay = models.CharField(max_length=30)

class XglUser(models.Model):
    uid = models.IntegerField()
    telephone = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    """docstring for """
    def __str__(self):
        return self.uid


class lbrUser(models.Model):
    uid = models.IntegerField()
    telephone = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    """docstring for """
    def __str__(self):
        return self.uid
        