# Generated by Django 3.0.8 on 2020-08-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_auto_20200828_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]