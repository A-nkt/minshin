from django.urls import path

from . import views


app_name = "details"
urlpatterns = [path('ans_past/<str:univ>/<str:subject>/<str:year>/', views.comment_form)]
