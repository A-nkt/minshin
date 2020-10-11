from django.shortcuts import render
from .forms import CommentForm
from .models import Comment,Image
from django_pandas.io import read_frame
import datetime
import pandas as pd

def IntengerChecker(val):#整数を二桁に直す関数
    val=int(val)
    if val <= 9:
        val='0'+str(val)
    else:
        val=str(val)
    return val

# Create your views here.
def comment_form(request,univ,subject_and_year):
    text=''
    user = str(request.user)
    if request.method == 'POST':#フォームが送信された時
        if str(user) =='AnonymousUser' and request.POST['name']!='管理人':#ログイン×管理人以外を使用している時
            form = CommentForm(request.POST)#送られたFormを変数に格納
            if form.is_valid():
                obj = form.save(commit=False)
                obj.univ=univ
                obj.subject_year=subject_and_year
                obj.date = datetime.datetime.now().date()
                obj.save()
                return render(request,'details/details_page_landing.html')
        elif str(user) =='AnonymousUser' and request.POST['name']=='管理人':#ログインしていないユーザーが管理人を使用する時
            form = CommentForm()
            text='管理人は使用することができません。'
        elif str(user) !='AnonymousUser' and request.POST['name']=='管理人':#ユーザーがログインしている時
            form = CommentForm(request.POST)#送られたFormを変数に格納
            if form.is_valid():
                obj = form.save(commit=False)
                obj.univ=univ
                obj.subject_year=subject_and_year
                obj.date = datetime.datetime.now().date()
                obj.save()
                return render(request,'details/details_page_landing.html')
        else:#ユーザーがログインしていて管理人意外
            form = CommentForm()
    else:#フォームが送信されていない場合
        form = CommentForm()
    data=Comment.objects.all().filter(univ=univ,subject_year=subject_and_year)
    df=read_frame(data)
    df=df.reset_index(drop=True)
    for i in range(len(df)):
        if i%2==0:
            df.loc[i,'odd']=False
        else:
            df.loc[i,'odd']=True
    #print(df)
    #img=Image.objects.all().filter(univ=univ,subject_year=subject_and_year)
    #img=read_frame(img)
    #print(img)
    img="";img2=""
    if univ=="nagoya-u" and subject_and_year=="physics2019":
        img="img/startup-593327_1920.jpg"
        img2="img/startup-593327_1920.jpg"

    context={
        'form':form,
        'df':df,
        'text':text,
        'Img':img,
        'Img2':img2,
        }
    return render(request, 'details/details_page.html',context)
