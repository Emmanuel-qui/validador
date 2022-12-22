from django.urls import path
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
   path('logout/', views.CustomLogoutView.as_view(), name="logout"),
   path('password_reset/', views.CustomPasswordResetView.as_view(), name="password_reset"),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


 