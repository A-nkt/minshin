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
    CONFIDENCE = (
            (1, '合ってる(8割)'),
            (2, '概ね合ってる（6割）'),
            (3, 'あまり合っていない（４割）'),
            (4, '合ってない(４割以下)'),
        )

    name=models.CharField(blank=True,null=True, max_length=100,help_text="name")
    message = models.TextField(max_length=300)
    date = models.DateField(verbose_name='打刻日')
    rate = models.IntegerField(verbose_name='正答率', choices=CONFIDENCE, default=None)
