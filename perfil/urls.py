from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='home'),

    path('user/', views.UserView.as_view()),
]