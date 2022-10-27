from unicodedata import name
from django.shortcuts import render

from django.urls import path

from . import views

# Create your urls here.

app_name = 'validate'

urlpatterns = [
	
	path('', views.IndexView.as_view(), name="index"),

	path('result/', views.ResultValidate.as_view(), name="result")
]