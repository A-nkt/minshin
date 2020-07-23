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

class FormField(AbstractFormField):
    FORM_FIELD_CHOICES = list(FORM_FIELD_CHOICES) + [('document', 'Upload Document')]
    # `field_type` and `page` remain unchanged


class ExtendedFormBuilder(FormBuilder):
    def create_document_upload_field(self, field, options):
        return FileField(**options)
    FIELD_TYPES = FormBuilder.formfields

class FormPage(AbstractEmailForm):
    # `form_builder` attribute and `serve` remain unchanged.

    def process_form_submission(self, form):
        cleaned_data = form.cleaned_data

        for name, field in form.fields.iteritems():
            if isinstance(field, FileField):
                document_file_data = cleaned_data[name]
                if document_file_data:
                    DocumentModel = get_document_model()
                    document = DocumentModel(
                        file=cleaned_data[name],
                        title=filename_to_title(cleaned_data[name].name),
                        # assumes there is always a user - will fail otherwise
                        uploaded_by_user=form.user,
                    )
                    document.save()
                    cleaned_data.update({name: document.id})
                else:
                    # remove the value from the data
                    del cleaned_data[name]

        # The rest of the function is unchanged

class FormField(AbstractFormField):
    FORM_FIELD_CHOICES = list(FORM_FIELD_CHOICES) + [('document', 'Upload Document')]
    Page=ParentalKey(
        'Uploadpage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class UploadPage(AbstractEmailForm):
    template="upload/upload_page.html"

    intro=RichTextField(blank=True)
    thank_you_text=RichTextField(blank=True)
    icon = models.FileField(upload_to='icon/', null=True, blank=True)

    content_panels=AbstractEmailForm.content_panels+[
        FieldPanel('intro'),
        InlinePanel('form_fields',label='Form Fields'),
        FieldPanel('thank_you_text'),
        FieldPanel('icon'),
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

class File(models.Model):
    #picture = CloudinaryField('image')
    icon = models.FileField(upload_to='icon/', null=True, blank=True)
