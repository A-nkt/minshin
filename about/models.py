from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks

#みんなの院試についての紹介ページ
class AboutPage(Page):
    template = "about/about_page.html"#対応するhtmlファイルを指定

    banner_title = models.CharField(max_length = 100,blank = True,null = True)#文字列のフィールドを定義
    banner_subtitle = RichTextField(features = ["bold","italic"],blank = True)#太字やその他色々な機能があるRichTextFieldを定義
    banner_image = models.ForeignKey(#画像用のフィールドを定義
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    content = StreamField(#Blockを使って、要素が可変的なモデルを定義
        [
            ("title",blocks.AboutTitleBlock()),
        ],
        null = True,
        blank = True
    )

    content_panels = Page.content_panels+[#上記で定義した各フィールドを各Panelとして定義
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel('content'),
    ]
