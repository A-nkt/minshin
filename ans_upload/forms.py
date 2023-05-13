from django import forms
from .models import File


# modelからFormを作る
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('title', 'subtitle', 'subfield', 'subject', 'year', 'file', 'file2', 'file3', 'file4', 'file5')  # 大学、研究科、専攻、教科、年度、データがフォームの対象
