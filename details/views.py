from django.shortcuts import render
from .forms import CommentForm
from .models import Comment,Image
from django_pandas.io import read_frame
import datetime
import pandas as pd
import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='My Project 72481-3295e714262b.json'

def IntengerChecker(val):#整数を二桁に直す関数
    val=int(val)
    if val <= 9:
        val='0'+str(val)
    else:
        val=str(val)
    return val

# Create your views here.
def comment_form(request,univ,subject,year):
    subject_and_year=subject+year
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

    img_df=read_frame(Image.objects.all().filter(univ=univ,subject_year=subject_and_year))
    img_link=[]
    for j in range(len(img_df)):
        iglink=img_df.loc[j,'answer']
        iglink=iglink.split('/')[1]
        img_link.append(iglink)

    dx=pd.DataFrame(columns={'img'});i=0
    for ig in img_link:
        object_name='upload/'+ig
        bucket_name = "minshin"

        outfile = 'minshin/static/img/'+ig
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.download_to_filename(outfile)
        dx.loc[i,'img']='/static/img/'+ig
        i+=1

    if subject == "math":
        content="数学"+year
    elif subject == "physics":
        content="物理"+year
    elif subject == "chemistry":
        content="化学"+year
    elif subject == "condensed_matter_physics":
        content = "物性物理学" + year
    else:
        content=""

    if univ == "nagoya-u":
        univ_name = "名古屋大学"
    elif univ == "tokyo-u":
        univ_name = "東京大学"
    elif univ == "hokkaido-u":
        univ_name = "北海道大学"
    elif univ == "tohoku-u":
        univ_name = "東北大学"
    elif univ == "osaka-u":
        univ_name = "大阪大学"
    elif univ == "kyoto-u":
        univ_name = "京都大学"
    elif univ == "kyushu-u":
        univ_name = "九州大学"
    elif univ == "tokyo-city-u":
        univ_name = "東京都立大学"
    elif univ == "waseda-u":
        univ_name = "早稲田大学"
    elif univ == "keio-u":
        univ_name = "慶應義塾大学"
    elif univ == "jochi-u":
        univ_name = "上智大学"
    else:
        univ_name = ""

    context={
        'form':form,
        'df':df,
        'text':text,
        'dx':dx,
        'content':content,
        'univ_name':univ_name,
        'univ':univ,
        }
    return render(request, 'details/details_page.html',context)
