# Generated by Django 3.0.8 on 2020-08-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
