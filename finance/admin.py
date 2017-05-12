from django.contrib import admin

from .models import Users, Consumption_record, Recharge_record, XglUser, lbrUser

class UsersAdmin(admin.ModelAdmin):
    fields = ['moneys','telephone','invitation','uid']
    list_display = ('uid','telephone','moneys','new_awards')


class Consumption_recordAdmin(admin.ModelAdmin):
    list_display = ('uid','user_id','amount','group_id','create_at')

class Recharge_recordAdmin(admin.ModelAdmin):
    list_display = ('uid','user_id','amount','pay','create_at','status','out_no')

class XglUserAdmin(admin.ModelAdmin):
    list_display = ('uid','name','telephone')
    
class lbrUserAdmin(admin.ModelAdmin):
    list_display = ('uid','name','telephone')

admin.site.register(Users, UsersAdmin)
admin.site.register(Consumption_record,Consumption_recordAdmin)
admin.site.register(Recharge_record,Recharge_recordAdmin)
admin.site.register(XglUser, XglUserAdmin)
admin.site.register(lbrUser, lbrUserAdmin)