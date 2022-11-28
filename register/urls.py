from django.urls import include, path, re_path
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path(
       "activate/complete/",
       TemplateView.as_view(
           template_name="django_registration/activation_complete.html"
       ),
       name="django_registration_activation_complete",
   ),
   path(
       "activate/<str:activation_key>/",
       views.ActivationView.as_view(),
       name="django_registration_activate",
   ),
   path(
       "register/",
       views.RegistrationView.as_view(),
       name="django_registration_register",
   ),
   path(
       "register/complete/",
       TemplateView.as_view(
           template_name="django_registration/registration_complete.html"
       ),
       name="django_registration_complete",
   ),
   path(
       "register/closed/",
       TemplateView.as_view(
           template_name="django_registration/registration_closed.html"
       ),
       name="django_registration_disallowed",
   ),

    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),

    path('password_change/', views.ChangePasswordForm.as_view(), name="change_password")
]