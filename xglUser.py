#!/usr/bin/env python
#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
 
import json
import django
import datetime
import time
import pandas as pd
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
 


def loadXgxzUser():
    from finance.models import XglUser
    # import pdb; pdb.set_trace()
    data = pd.read_csv('xgxz.csv')
    for i in range(1000):
        uid = data['编号'][i]
        name = data['微信名称'][i]
        telephone = data['电话号码'][i]
        XglUser.objects.create(uid=uid, telephone=telephone, name=name)

def loadLbrUser():
    from finance.models import lbrUser
    import pdb; pdb.set_trace()
    data = pd.read_csv('lbr.csv')
    for i in range(1000):
        uid = data['序号'][i]
        name = data['用户名'][i]
        telephone = data['手机号码'][i]
        lbrUser.objects.create(uid=uid, telephone=telephone, name=name)

def deleteLbrUserPay():
    from finance.models import lbrUser
    lbrUser.objects.all().delete()

def deleteXglUserPay():
    from finance.models import XglUser
    XglUser.objects.all().delete()


def popUser():
    from finance.models import lbrUser, XglUser
    xgxzUser = XglUser.objects.all()
    xgxzIphone = []
    for item in xgxzUser:
        telephone = item.telephone
        xgxzIphone.append(telephone)
    lbrUserList = lbrUser.objects.all()
    import pdb; pdb.set_trace()
    lbrUser.objects.filter(telephone=0).delete()
    for item in lbrUserList:
        telephone = item.telephone
        if telephone in xgxzIphone:
            lbrUser.objects.filter(telephone=telephone).delete()

def writeUser():
    import xlwt
    from finance.models import lbrUser
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    lbrUserList = lbrUser.objects.all()
    # write info
    i=0
    for item in lbrUserList:
        worksheet.write(i, 0, label = item.uid)
        worksheet.write(i, 2, label = item.telephone)
        worksheet.write(i, 1, label = item.name)
        i=i+1
    workbook.save('Excel_Workbook.xls')
   
if __name__ == "__main__":
    # deleteLbrUserPay()
    # deleteXglUserPay()
    # loadXgxzUser()
    # loadLbrUser()
    # popUser()
    writeUser()

    # main()
    # consumption()
    # recharge_record()
    print('Done!')