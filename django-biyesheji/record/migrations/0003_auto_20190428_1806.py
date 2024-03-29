# Generated by Django 2.1.1 on 2019-04-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20190423_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record_user',
            options={'verbose_name': '学生记录管理', 'verbose_name_plural': '学生记录管理'},
        ),
        migrations.AlterModelOptions(
            name='record_visitor',
            options={'verbose_name': '外来人员记录管理', 'verbose_name_plural': '外来人员记录管理'},
        ),
        migrations.AddField(
            model_name='record_visitor',
            name='idcard',
            field=models.CharField(default=362500199901010000, max_length=64, verbose_name='身份证号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record_user',
            name='in_out',
            field=models.CharField(choices=[('进', '进'), ('出', '出')], max_length=32, verbose_name='进出'),
        ),
        migrations.AlterField(
            model_name='record_user',
            name='remark',
            field=models.CharField(max_length=256, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='record_user',
            name='stu_no',
            field=models.CharField(max_length=128, verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='record_user',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='record_visitor',
            name='in_out',
            field=models.CharField(choices=[('进', '进'), ('出', '出')], max_length=32, verbose_name='进出'),
        ),
        migrations.AlterField(
            model_name='record_visitor',
            name='phone',
            field=models.CharField(max_length=128, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='record_visitor',
            name='remark',
            field=models.CharField(max_length=256, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='record_visitor',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='record_visitor',
            name='visitor_name',
            field=models.CharField(max_length=128, verbose_name='姓名'),
        ),
    ]
