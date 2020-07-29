from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm

# Create your models here.
class RulePage(Page):
    template="rule/rule_page.html"

    rule_text=RichTextField(blank=True)

    content_panels=Page.content_panels+[
        FieldPanel('rule_text'),
    ]
