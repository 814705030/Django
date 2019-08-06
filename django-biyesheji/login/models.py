from django.db import models


# Create your models here.


class User(models.Model):
    # 用户表

    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    stu_no = models.CharField('学号', max_length=128, unique=True)
    name = models.CharField('姓名', max_length=128)
    sex = models.CharField('性别', max_length=32, choices=gender)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', max_length=256)
    phone = models.CharField('电话', max_length=128)
    dorm_name = models.CharField('宿舍楼', max_length=128, unique=True)
    dorm_no = models.CharField('门牌号', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
