from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks

# Create your models here.
class AboutPage(Page):
    template="about/about_page.html"

    banner_title=models.CharField(max_length=100,blank=True,null=True)
    banner_subtitle=RichTextField(features=["bold","italic"],blank=True)
    banner_image=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content=StreamField(
        [
            ("title",blocks.AboutTitleBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels=Page.content_panels+[
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel('content'),
    ]
