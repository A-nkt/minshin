from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks

# Create your models here.
class RulePage(Page):
    template="rule/rule_page.html"

    rule_content=StreamField(
        [
            ("title",blocks.RuleTitleBlock()),
            ("date",blocks.RuleDate()),
        ],
        null=True,
        blank=True,
    )

    content_panels=Page.content_panels+[
        StreamFieldPanel('rule_content'),
    ]
