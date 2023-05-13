from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


# みんなのTOEICアップロードページ
class FormField(AbstractFormField):
    Page = ParentalKey(
        'MintoContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class MintoContactPage(AbstractEmailForm):
    template = "minto/minto_contact_page.html"
    landing_page_template = "minto/minto_page_landing.html"

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label='Form Fields'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
