from django.db import models

# Create your models here.
gender = (('进', '进'), ('出', '出'))


class record_user(models.Model):
    stu_no = models.CharField('学号', max_length=128)
    time = models.DateTimeField('时间', auto_now_add=True, )
    in_out = models.CharField('进出', max_length=32, choices=gender)
    remark = models.CharField('备注', max_length=256)

    class Meta:
        verbose_name = '学生记录管理'
        verbose_name_plural = '学生记录管理'


class record_visitor(models.Model):
    visitor_name = models.CharField('姓名', max_length=128)
    time = models.DateTimeField('时间', auto_now_add=True, )
    in_out = models.CharField('进出', max_length=32, choices=gender)
    idcard = models.CharField('身份证号', max_length=64)
    remark = models.CharField('备注', max_length=256)
    phone = models.CharField('电话', max_length=128)

    class Meta:
        verbose_name = '外来人员记录管理'
        verbose_name_plural = '外来人员记录管理'
