from django.urls import path

from . import views

urlpatterns = [
    path('ans_upload/', views.ans_upload, name='ans_file_upload'),#アップロードURL
]
