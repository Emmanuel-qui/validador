from django.urls import include, path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
       "accounts/activate/complete/",
       TemplateView.as_view(
           template_name="django_registration/activation_complete.html"
       ),
       name="django_registration_activation_complete",
   ),
   path(
       "accounts/activate/<str:activation_key>/",
       views.ActivationView.as_view(),
       name="django_registration_activate",
   ),
   path(
       "accounts/register/",
       views.RegistrationView.as_view(),
       name="django_registration_register",
   ),
   path(
       "accounts/register/complete/",
       TemplateView.as_view(
           template_name="django_registration/registration_complete.html"
       ),
       name="django_registration_complete",
   ),
   path(
       "accounts/register/closed/",
       TemplateView.as_view(
           template_name="django_registration/registration_closed.html"
       ),
       name="django_registration_disallowed",
   ),

    path('accounts/', include('django.contrib.auth.urls')),
]