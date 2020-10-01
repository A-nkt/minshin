from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name="details"


urlpatterns = [
    path('ans_past/nagoya-u/physics2019/',views.comment_form),
    ]
