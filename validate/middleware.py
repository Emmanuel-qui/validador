from django.shortcuts import redirect

from perfil.models import AccountModel


class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response


    def process_view(self,request, view_func, view_args, view_kwargs):
        
        url = request.META.get('PATH_INFO')
        if request.user.is_authenticated:
            obj_user = request.user
            obj_account = AccountModel.objects.filter(user=obj_user.id) 

            if url == "/validate/" and not obj_account.exists():
                return redirect("/profile/informacion/")
            elif url == "/validate/result/" and not obj_account.exists():
                return redirect("/profile/informacion/")
        


        