from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks

# Create your models here.
class MintoPage(Page):
    template="minto/minto_page.html"

    subpage_types=[
    'ContentsPage',
    ]

    UNIV=StreamField(#Blockを使って、要素が可変的なモデルを定義
        [("UNIV",blocks.MintoUniversity())],
        null=True,blank=True,
    )

    content_panels=Page.content_panels+[
        StreamFieldPanel('UNIV'),
    ]

class ContentsPage(MintoPage):
    template="minto/contents.html"#対応するhtmlファイルを指定

    INDEX=StreamField(#Blockを使って、要素が可変的なモデルを定義
        [
            ("INDEX",blocks.MintoContentIndex()),
        ],
        null=True,
        blank=True,
    )
    VALUE=StreamField(#Blockを使って、要素が可変的なモデルを定義
        [
            ("INDEX",blocks.MintoContentValue()),
        ],
        null=True,
        blank=True,
    )
    content_panels=Page.content_panels+[
        StreamFieldPanel('INDEX'),
        StreamFieldPanel('VALUE'),
    ]
