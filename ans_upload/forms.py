from django import forms
from .models import File

class FileForm(forms.ModelForm):#modelからFormを作る
    class Meta:
        model = File
        fields = ('title','subtitle','subfield','subject','year','file',)
