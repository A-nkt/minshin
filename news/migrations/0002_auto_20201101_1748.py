# Generated by Django 3.0 on 2020-11-01 08:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='main_title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('newspage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.NewsPage')),
                ('main_text', wagtail.core.fields.RichTextField(blank=True, max_length=300, null=True, verbose_name='メインコンテンツ')),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('year', models.IntegerField(default=2020)),
                ('ヘッダー画像', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('news.newspage',),
        ),
    ]