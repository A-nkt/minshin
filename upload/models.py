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
from django.forms import FileField
from wagtail.documents.models import get_document_model
from wagtail.contrib.forms.models import FORM_FIELD_CHOICES
from wagtail.contrib.forms.forms import FormBuilder
# Create your models here.

# Other imports

    # `field_type` and `page` remain unchanged




        # The rest of the function is unchanged

class FormField(AbstractFormField):
    #FORM_FIELD_CHOICES = list(FORM_FIELD_CHOICES) + [('document', 'ファイルアップロード')]
    CHOICES = list(FORM_FIELD_CHOICES) + [('document', 'ファイルアップロード')]
    Page=ParentalKey(
        'Uploadpage',
        on_delete=models.CASCADE,
        related_name='form_fields',
        #choices=CHOICES
    )

class CustomFormBuilder(FormBuilder):
    # create a function that returns an instanced Django form field
    # function name must match create_<field_type_key>_field
    def create_ipaddress_field(self, field, options):
        # return `forms.GenericIPAddressField(**options)` not `forms.SlugField`
        # returns created a form field with the options passed in
        return forms.GenericIPAddressField(**options)

class UploadPage(AbstractEmailForm):
    
    template="upload/upload_page.html"

    intro=RichTextField(blank=True)
    thank_you_text=RichTextField(blank=True)
    #icon = models.FileField(upload_to='icon/', null=True, blank=True)

    content_panels=AbstractEmailForm.content_panels+[
        FieldPanel('intro'),
        InlinePanel('form_fields',label='Form Fields'),
        FieldPanel('thank_you_text'),
        #FieldPanel('icon'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address',classname="col6"),
                FieldPanel('to_address',classname='col6'),
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),

    ]
    form_builder = CustomFormBuilder

    #class Meta:
        #verbose_name="Upload Page"
        #verbose_name_plural="Upload Pages"


"""
class FormField(AbstractFormField):
    # extend the built in field type choices
    # our field type key will be 'ipaddress'
    CHOICES = FORM_FIELD_CHOICES + (('ipaddress', 'IP Address'),)

    page = ParentalKey('FormPage', related_name='form_fields')
    # override the field_type field with extended choices
    field_type = models.CharField(
        verbose_name='field type',
        max_length=16,
        # use the choices tuple defined above
        choices=CHOICES
    )


class CustomFormBuilder(FormBuilder):
    # create a function that returns an instanced Django form field
    # function name must match create_<field_type_key>_field
    def create_ipaddress_field(self, field, options):
        # return `forms.GenericIPAddressField(**options)` not `forms.SlugField`
        # returns created a form field with the options passed in
        return forms.GenericIPAddressField(**options)


class FormPage(AbstractEmailForm):
    # intro, thank_you_text, edit_handlers, etc...

    # use custom form builder defined above
    form_builder = CustomFormBuilder
"""
