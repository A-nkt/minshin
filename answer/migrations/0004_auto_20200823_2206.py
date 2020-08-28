# Generated by Django 3.0.8 on 2020-08-23 13:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0003_auto_20200822_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerpage',
            name='five',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True))])), ('full_richtext', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True)), ('links', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answerpage',
            name='four',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True))])), ('full_richtext', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True)), ('links', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answerpage',
            name='second',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True))])), ('full_richtext', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True)), ('links', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answerpage',
            name='third',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True))])), ('full_richtext', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Add about content', max_length=1000, null=True)), ('links', wagtail.core.blocks.CharBlock(blank=True, help_text='Add about title', max_length=100, null=True))]))], blank=True, null=True),
        ),
    ]