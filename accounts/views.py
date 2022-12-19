from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    
    redirect_authenticated_user = True
