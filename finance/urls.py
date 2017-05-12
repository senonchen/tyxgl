from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^step1/', views.step1, name='step1'),
    url(r'^step2/', views.step2, name='step2'),
    url(r'^auto/', views.autorun, name='autorun'),
    url(r'^delete/',views.delete_data, name='delete_data'),
    url(r'^recharge_record/',views.recharge_record, name='recharge_record'),
    url(r'^neimeng_recharge_record/',views.neimeng_recharge_record, name='neimeng_recharge_record'),
    url(r'^neimeng_consumption/',views.neimeng_consumption_record, name='neimeng_consumption_record'),
    
    
]