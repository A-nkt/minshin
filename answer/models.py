from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks


# 各大学の5年分が対象となる
class AnswerPage(Page):
    template = "answer/answer_page.html"
    year_2020 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True,
    )
    year_2019 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True,
    )
    year_2018 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    year_2017 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    year_2016 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    year_2015 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    # 2014
    year_2014 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    # 2013
    year_2013 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    # 2012
    year_2012 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )
    # 2011
    year_2011 = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlockAns()),
            ("full_richtext", blocks.RichtextBlockAns()),
        ],
        null=True, blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('year_2020'),
        StreamFieldPanel('year_2019'),
        StreamFieldPanel('year_2018'),
        StreamFieldPanel('year_2017'),
        StreamFieldPanel('year_2016'),
        StreamFieldPanel('year_2015'),
        StreamFieldPanel('year_2014'),
        StreamFieldPanel('year_2013'),
        StreamFieldPanel('year_2012'),
        StreamFieldPanel('year_2011'),
    ]

    class Meta:
        verbose_name = "Answer Page"
        verbose_name_plural = "Answer Pages"
