# Generated by Django 3.0.8 on 2020-08-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_auto_20200828_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default='2020-01-01', verbose_name='打刻日'),
            preserve_default=False,
        ),
    ]