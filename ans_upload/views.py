from django.shortcuts import render
from .forms import FileForm
from .models import File
from django.core.mail import send_mail


def ans_upload(request):
    obj = File()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            subject = "過去問アップロード<みんなの院試>"  # 題名
            message = "みんなの院試です。\n 過去問解答を受領しました。確認してください。\n https://minshin.net/admin"  # 本文
            from_email = ""
            recipient_list = ["minshin@gmail.com"]
            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'ans_upload/ans_upload_page_landing.html')
    else:
        form = FileForm()
    return render(request, 'ans_upload/ans_upload.html', {'form': form})
