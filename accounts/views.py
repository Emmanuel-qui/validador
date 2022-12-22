from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import LogoutView


class CustomLoginView(LoginView):
    
    redirect_authenticated_user = True


class CustomPasswordResetView(PasswordResetView):

    html_email_template_name = "registration/password_reset_email.html"



class CustomLogoutView(LogoutView):
    next_page = "/"
    



