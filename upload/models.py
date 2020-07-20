from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

# Create your models here.
class FormField(AbstractFormField):
    Page=ParentalKey(
        'Uploadpage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class UploadPage(AbstractEmailForm):
    template="upload/upload_page.html"

    intro=RichTextField(blank=True)
    thank_you_text=RichTextField(blank=True)

    content_panels=AbstractEmailForm.content_panels+[
        FieldPanel('intro'),
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
    class Meta:
        verbose_name="Upload Page"
        verbose_name_plural="Upload Pages"
