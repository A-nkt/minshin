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
    AbstractFormField
)

# Create your models here.
class FormField(AbstractFormField):
    Page = ParentalKey(
        'JobPage',
        on_delete = models.CASCADE,
        related_name = 'form_fields',
    )

class JobPage(AbstractEmailForm):
    template = "job/job_page.html"

    intro = RichTextField(blank = True)
    text = RichTextField(blank = True)
    thank_you_text = RichTextField(blank = True)

    content_panels = AbstractEmailForm.content_panels+[
        FieldPanel('intro'),
        FieldPanel('text'),
        InlinePanel('form_fields',label = 'Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address',classname = "col6"),
                FieldPanel('to_address',classname = 'col6'),
            ]),
            FieldPanel('subject'),
        ], heading = "Email Settings"),

    ]
