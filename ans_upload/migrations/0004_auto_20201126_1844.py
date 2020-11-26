# Generated by Django 3.0 on 2020-11-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans_upload', '0003_auto_20201003_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='year',
            field=models.IntegerField(default=2019, help_text='<p>解答した年を入力してください<br>(例)2020年入学者用問題→2019年</p>', verbose_name='年度'),
        ),
    ]