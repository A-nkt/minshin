# Generated by Django 3.0.8 on 2020-07-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0003_auto_20200721_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='univpage',
            name='major1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]