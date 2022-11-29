from django.urls import include, path, re_path
from django.views.generic import TemplateView


from . import views


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
       "",
       views.RegistrationView.as_view(),
       name="django_registration_register",
   ),
   path(
       "complete/",
       TemplateView.as_view(
           template_name="django_registration/registration_complete.html"
       ),
       name="django_registration_complete",
   ),
   path(
       "closed/",
       TemplateView.as_view(
           template_name="django_registration/registration_closed.html"
       ),
       name="django_registration_disallowed",
   ),

    
]