# Generated by Django 3.0.8 on 2020-08-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20200829_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, help_text='name', max_length=100, null=True),
        ),
    ]
