# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Consumption_record, Users, Recharge_record
import datetime
import time
import django.utils.timezone as timezone
timezone.deactivate()
# Create your views here.
def step1(request):
    cobj = Consumption_record.objects.all()
    for item in cobj:
        # import pdb; pdb.set_trace()
        user_id = item.user_id.uid	
        user = Users.objects.get(uid=user_id)
        user.save()
    return HttpResponse('Done') 
    

def amount(record,info):
    amounts = 0
    for item in record:
        amounts = amounts+float(item.amount)
    amounts_exclude = amounts-info['new']*30
    amount_info = {'amounts':amounts, 'amounts_exclude':amounts_exclude}
    return amount_info

def step2(request):
    # 设置时间
    start_time = datetime.datetime(2017,01,01,0,0,0)
    end_time = datetime.datetime(2017,02,01,0,0,0)
    #筛选符合条件的线下消费记录
    neimeng_cr = Consumption_record.objects.filter(group_id=2).filter(create_at__gt=start_time).filter(create_at__lt=end_time)
    pre_neimeng_cr = Consumption_record.objects.filter(create_at__lt=start_time)
    new_customer = 0   
    old_customer = 0
    #计算此时间段有多少用户产生了消费
    user_id_list=[]
    for item in neimeng_cr:
        uid = item.user_id.uid
        user_id_list.append(uid)
    new_user_id = list(set(user_id_list))
    new_user_id.sort()
    #比对用户是否之前消费过，并计算新用户数目
    for item in new_user_id:
        if not Consumption_record.objects.filter(create_at__lt=start_time).filter(uid=item):
            new_customer = new_customer+1
        else:
            old_customer = old_customer+1
    len_neimeng_cr = len(neimeng_cr)
    info = {'new':new_customer,'old':old_customer,'len':len_neimeng_cr}
    amounts = amount(neimeng_cr, info)
    return render(request, 'shishou.html', {'TutorialList': user_id_list,'new_user_id':new_user_id,'info':info,'amounts':amounts})

def recharge_record(request):
    start_time = datetime.datetime(2017,03,01,0,0,0)
    end_time = datetime.datetime(2017,04,01,0,0,0)
    rr = Recharge_record.objects.filter(create_at__gt=start_time).filter(create_at__lt=end_time).filter(status=1)
    pay = 0
    for item in rr:
        pay = pay + float(item.pay)
        print('%s--%s'%(item.pay,item.uid))
        if item.pay==0.01:
            print('%s'%item.uid)
    return HttpResponse(pay)

def delete_data(request):
    Users.objects.all().delete()
    return HttpResponse('delete Done!')

def neimeng_userid():
     # 设置时间
    start_time = datetime.datetime(2017,03,01,0,0,0)
    end_time = datetime.datetime(2017,04,07,0,0,0)
    #筛选符合条件的线下消费记录
    neimeng_cr = Consumption_record.objects.filter(group_id=2).filter(create_at__gt=start_time).filter(create_at__lt=end_time)
    new_customer = 0   
    old_customer = 0
    #计算此时间段有多少用户产生了消费
    user_id_list=[]
    for item in neimeng_cr:
        uid = item.user_id.uid
        user_id_list.append(uid)
    new_user_id = list(set(user_id_list))
    new_user_id.sort()
    return new_user_id

def neimeng_recharge_record(request):
    # import pdb; pdb.set_trace()
    user_id = neimeng_userid()
    start_time = datetime.datetime(2017,04,01,0,0,0)
    end_time = datetime.datetime(2017,04,07,0,0,0)
    rr = Recharge_record.objects.filter(create_at__gt=start_time).filter(create_at__lt=end_time).filter(status=1)
    pay = 0
    pay1 = 0
    recharge_record = []
    recharge_record_bj = []
    for item in rr:
        # pay = pay + float(item.pay)
        if item.user_id.uid in user_id:
            recharge_record.append(item)
            pay = pay + float(item.pay)
        else:
            recharge_record_bj.append(item)
            pay1 = pay1 + float(item.pay)

    return HttpResponse('内蒙充值金额%s'%(pay1))
    # return render(request, 'neimeng.html', {'recharge_record':recharge_record,'recharge_record_bj':recharge_record_bj, 'pay':pay, 'pay1':pay1})


def neimeng_consumption_record(request):
    start_time = datetime.datetime(2017,03,01,0,0,0)
    end_time = datetime.datetime(2017,04,01,0,0,0)
    neimeng_cr = Consumption_record.objects.filter(group_id=0).filter(create_at__gt=start_time).filter(create_at__lt=end_time)
    # amounts = 0
    # for item in neimeng_cr:
    #     amounts = float(item.amount)+amounts

    # beijing_cr = Consumption_record.objects.filter(group_id=0).filter(create_at__gt=start_time).filter(create_at__lt=end_time)
    # amounts_bj = 0
    # for item in beijing_cr:
    #     amounts_bj = float(item.amount)+amounts_bj

    # return HttpResponse(amounts_bj)

    return render(request, 'neimeng_consuption.html', {'neimeng_cr':neimeng_cr})





def autorun(request):
    step1()
    step2()


