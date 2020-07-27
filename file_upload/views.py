from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from django.http import HttpResponse
from .models import File
import sys

# ------------------------------------------------------------------
def file_upload(request):
    obj=File()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'file_upload/upload_page_landing.html')
    else:
        form = FileForm()
    return render(request, 'file_upload/upload.html', {'form': form})
