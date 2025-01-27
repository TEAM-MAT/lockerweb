# Generated by Django 4.0.1 on 2022-02-28 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0005_department_fintime_alter_department_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='fintime',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 5, 22, 41, 14, 907800), help_text='예약 종료 날짜'),
        ),
        migrations.AlterField(
            model_name='department',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 22, 41, 14, 907781), help_text='예약시작날짜'),
        ),
    ]
