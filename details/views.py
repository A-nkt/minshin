import datetime
import os

from django.shortcuts import render, redirect
from django_pandas.io import read_frame
from google.cloud import storage
import pandas as pd

from .forms import CommentForm
from .models import Comment, Image


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '******.json'


# 整数を二桁に直す関数
def IntengerChecker(val):
    return '0' + str(int(val)) if val <= 9 else str(int(val))


def subject_to_content(subject, year):
    if subject == "math":
        content = "数学" + year
    elif subject == "physics":
        content = "物理" + year
    elif subject == "chemistry":
        content = "化学" + year
    elif subject == "condensed_matter_physics":
        content = "物性物理学" + year
    elif subject == "math_kiso":
        content = "数理学専攻　数学（基礎）" + year
    elif subject == "math_senmon":
        content = "数理学専攻　数学（専門）" + year
    else:
        content = ""
    return content


def univ_to_name(univ):
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
    return univ_name


def comment_form(request: str, univ: str, subject: str, year: str):
    content, univ_name = subject_to_content(subject, year), univ_to_name(univ)

    subject_and_year = subject + year
    text = ''
    user = str(request.user)
    # フォームが送信された時
    if request.method == 'POST':
        if request.POST['rate'] == '0':
            return redirect('/ans_past/' + univ + '/' + subject + '/' + year + '/')
        # ログイン×管理人以外を使用している時
        if str(user) == 'AnonymousUser' and request.POST['name'] != '管理人':
            # 送られたFormを変数に格納
            form = CommentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.univ = univ
                obj.subject_year = subject_and_year
                obj.date = datetime.datetime.now().date()
                obj.save()
                context = {
                    'content': content,
                    'univ_name': univ_name,
                }
                return render(request, 'details/details_page_landing.html', context)
        # ログインしていないユーザーが管理人を使用する時
        elif str(user) == 'AnonymousUser' and request.POST['name'] == '管理人':
            form = CommentForm()
            text = '管理人は使用することができません。'
        # ユーザーがログインしている時
        elif str(user) != 'AnonymousUser' and request.POST['name'] == '管理人':
            # 送られたFormを変数に格納
            form = CommentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.univ = univ
                obj.subject_year = subject_and_year
                obj.date = datetime.datetime.now().date()
                obj.save()
                context = {
                    'content': content,
                    'univ_name': univ_name,
                }
                return render(request, 'details/details_page_landing.html', context)
        # ユーザーがログインしていて管理人意外
        else:
            form = CommentForm()
    # フォームが送信されていない場合
    else:
        form = CommentForm()
    data = Comment.objects.all().filter(univ=univ, subject_year=subject_and_year)
    df = read_frame(data)
    df = df.reset_index(drop=True)
    for i in range(len(df)):
        df.loc[i, 'odd'] = False if i % 2 == 0 else True

    img_df = read_frame(Image.objects.all().filter(univ=univ, subject_year=subject_and_year))
    img_link = []
    for j in range(len(img_df)):
        img_link.append(img_df.loc[j, 'answer'].split('/')[1])

    dx = pd.DataFrame(columns={'img'})
    i = 0
    for ig in img_link:
        object_name = 'upload/' + ig
        bucket_name = "minshin"

        outfile = 'minshin/static/img/' + ig
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(object_name)
        blob.download_to_filename(outfile)
        dx.loc[i, 'img'] = '/static/img/' + ig
        i += 1

    context = {
        'form': form,
        'df': df,
        'text': text,
        'dx': dx,
        'content': content,
        'univ_name': univ_name,
        'univ': univ
    }
    return render(request, 'details/details_page.html', context)
