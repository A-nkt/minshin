from django.shortcuts import render
from .forms import CommentForm
from .models import Comment
from django_pandas.io import read_frame
import datetime

def IntengerChecker(val):#整数を二桁に直す関数
    val=int(val)
    if val <= 9:
        val='0'+str(val)
    else:
        val=str(val)
    return val

# Create your views here.
def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.date = datetime.datetime.now().date()
            obj.save()
            return render(request,'details/details_page_landing.html')
    else:
        form = CommentForm()
    data=Comment.objects.all()
    df=read_frame(data)
    print(df)
    context={
        'form':form,
        'df':df,
        }
    return render(request, 'details/details_page.html',context)
