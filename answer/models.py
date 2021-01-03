from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks
# 各大学の5年分が対象となる
class AnswerPage(Page):
    template="answer/answer_page.html"
    year_2020=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True,
    )
    first=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True,
    )
    second=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    third=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    four=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    five=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    #2014
    six=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    #2013
    seven=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    #2012
    eight=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )
    #2011
    nine=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlockAns()),
            ("full_richtext",blocks.RichtextBlockAns()),
        ],
        null=True,
        blank=True
    )


    content_panels=Page.content_panels+[
        StreamFieldPanel('year_2020'),
        StreamFieldPanel('first'),
        StreamFieldPanel('second'),
        StreamFieldPanel('third'),
        StreamFieldPanel('four'),
        StreamFieldPanel('five'),
        StreamFieldPanel('six'),
        StreamFieldPanel('seven'),
        StreamFieldPanel('eight'),
        StreamFieldPanel('nine'),
    ]
    class Meta:
        verbose_name="Answer Page"
        verbose_name_plural="Answer Pages"
