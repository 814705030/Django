# Generated by Django 2.1.1 on 2019-04-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_no', models.CharField(max_length=128, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('in_out', models.CharField(choices=[('进', '进'), ('出', '出')], max_length=32)),
                ('remark', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='record_visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=128, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('in_out', models.CharField(choices=[('进', '进'), ('出', '出')], max_length=32)),
                ('remark', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=128)),
            ],
        ),
    ]