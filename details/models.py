from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
)
#コンテンツモデルと投稿モデルを別個に定義してみる
#参考になった
#この解答は、合ってる(8割)、概ね合ってる（6割）、あまり合っていない（４割）、合ってない(４割以下)
#
class Comment(models.Model):
    name=models.CharField(blank=True,null=True, max_length=100,help_text="name")
    message = models.TextField(max_length=300)
    date = models.DateField(verbose_name='打刻日')



"""
# Create your models here.
class FormField(AbstractFormField):#Formのフィールドを定義
    Page=ParentalKey(
        'DetailsPage',#反応させるclass名を入力
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class DetailsPage(AbstractEmailForm):#フォーム機能を実装したclassを定義
    template="details/details_page.html"
    landing_page_template = "details/details_page_landing.html"

    thank_you_text=RichTextField(blank=True)#RichTextFieldを定義
    subtitle=models.CharField(max_length=100,null=True,blank=True)
    university=models.CharField(max_length=100,null=True,blank=True)
    university_link=models.CharField(max_length=100,null=True,blank=True)

    content_panels=AbstractEmailForm.content_panels+[#adminのパネルを定義
        FieldPanel("subtitle"),
        FieldPanel("university"),
        FieldPanel("university_link"),

        InlinePanel('form_fields',label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address',classname="col6"),
                FieldPanel('to_address',classname='col6'),
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
    ]
    """
