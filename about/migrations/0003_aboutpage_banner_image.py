# Generated by Django 3.0.8 on 2020-07-29 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('about', '0002_auto_20200729_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]