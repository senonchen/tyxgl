#!/usr/bin/env python
#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
 
import json
import django
import datetime
import time
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
 
 
def main():
    from finance.models import Users
    f = open('users.json')
    fr=f.read()
    fa = json.loads(fr)
    for item in fa:
        telephone = item['telephone']
        money = item['money']
        uid = item['id']
        # import pdb; pdb.set_trace()
        created_at = item['created_at']
        date_time = datetime.datetime.strptime(created_at,'%Y-%m-%d %H:%M:%S')
        updated_at = item['updated_at']
        # Users.objects.create(telephone=telephone,moneys=money,uid=uid,create_at=date_time)
        Users.objects.create(telephone=telephone,moneys=money,uid=uid)

        # print(type(user))
        # user.moneys = money
        # user.created_at = created_at
        # user.updated_at = updated_at
        # user.save()



        # print('%s'%telephone)
    print(type(fa))
    f.close()

def consumption():
    from finance.models import Users,Consumption_record
    f = open('consumption_record.json')
    fr = f.read()
    fa = json.loads(fr)

    for item in fa: 
        # import pdb; pdb.set_trace()
        uid = item['id']
        user_id = item['user_id']
        user = Users.objects.get(uid=user_id)
        amount = item['amount']
        group_id = item['group_id']
        created_at = item['created_at']
        date_time = datetime.datetime.strptime(created_at,'%Y-%m-%d %H:%M:%S')
        Consumption_record.objects.create(uid=uid, user_id=user, amount=amount, group_id=group_id)
        Consumption_record.objects.filter(uid=uid).update(create_at=date_time)
    f.close()

def recharge_record():
    from finance.models import *
    f = open('recharge_record.json')
    fr = f.read()
    fa = json.loads(fr)
    for item in fa:
        uid = item['id']
        out_no = item['out_no']
        user_id = item['user_id']
        user = Users.objects.get(uid=user_id)
        amount = item['amount']
        status = item['status']
        create_at = item['created_at']
        date_time = datetime.datetime.strptime(create_at,'%Y-%m-%d %H:%M:%S')
        pay = item['pay']
        Recharge_record.objects.create(uid=uid, out_no=out_no, user_id=user,amount=amount,status=status,pay=pay)
        Recharge_record.objects.filter(uid=uid).update(create_at=date_time)
    f.close()


if __name__ == "__main__":
    main()
    consumption()
    recharge_record()
    print('Done!')