# Generated by Django 3.0.8 on 2020-07-19 14:54

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0004_auto_20200719_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'PLURAL NAME'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_cta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(default='Test text'),
            preserve_default=False,
        ),
    ]
