from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from streams import blocks
# Create your models here.
class Ans_univPage(Page):
    template="ans_univ/ans_univ_page.html"

    content=StreamField(
        [
            ("title_and_text",blocks.TitleAndTextBlock()),
            ("full_richtext",blocks.RichtextBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels=Page.content_panels+[
        StreamFieldPanel('content'),
    ]
    class Meta:
        verbose_name="Ans_univ Page"
        verbose_name_plural="Ans_univ Pages"
