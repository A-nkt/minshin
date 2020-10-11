from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name="details"


urlpatterns = [
    path('ans_past/<str:univ>/<str:subject_and_year>/',views.comment_form),
    ]
