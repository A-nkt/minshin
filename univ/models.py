from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
# Create your models here.
class UnivPage(Page):
    template="univ/univ_page.html"

    subtitle=models.CharField(max_length=100,null=True,blank=True)
    body=RichTextField(blank=True)
    major1=models.CharField(max_length=100,null=True,blank=True)

    content_panels=Page.content_panels+[
        FieldPanel("subtitle"),
        FieldPanel('body'),
        FieldPanel('major1'),
    ]
    class Meta:
        verbose_name="Univ Page"
        verbose_name_plural="Univ Pages"
