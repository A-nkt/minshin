# Generated by Django 3.0 on 2020-11-21 11:42

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201101_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='main_text',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=10000, null=True, verbose_name='メインコンテンツ'),
        ),
    ]
