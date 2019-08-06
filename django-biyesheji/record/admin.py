from django.contrib import admin
from .models import record_user, record_visitor

# Register your models here.
admin.site.site_header = '宿舍进出管理系统'  # 此处设置页面显示标题
admin.site.site_title = '管理员界面'  # 此处设置页面头部标题


@admin.register(record_user)
class record_userAdmin(admin.ModelAdmin):
    list_display = ['stu_no', 'time', 'in_out', 'remark']
    readonly_fields = ['stu_no', 'time', 'in_out', 'remark']
    # list_display[0].short_description = '学号'
    list_filter = ['stu_no', 'time']
    search_fields = ['stu_no', 'time']
    list_per_page = 5


@admin.register(record_visitor)
class record_visitorAdmin(admin.ModelAdmin):
    list_display = ['visitor_name', 'time', 'in_out', 'remark', 'idcard', 'phone']
    readonly_fields = ['visitor_name', 'time', 'in_out', 'remark', 'idcard', 'phone']
    list_filter = ['visitor_name', 'time', 'idcard']
    search_fields = ['visitor_name', 'time', 'idcard']
    list_per_page = 5
