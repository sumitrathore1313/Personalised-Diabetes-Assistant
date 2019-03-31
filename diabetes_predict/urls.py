from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('other5ques/<str:sex>', views.other5ques, name='other5ques')
]