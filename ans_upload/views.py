from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from django.http import HttpResponse
from .models import File
import sys

# ------------------------------------------------------------------
def ans_upload(request):
    obj=File()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'ans_upload/ans_upload_page_landing.html')
    else:
        form = FileForm()
    return render(request, 'ans_upload/ans_upload.html', {'form': form})
