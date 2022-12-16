from django.http import HttpResponseRedirect
from django.http import JsonResponse


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


from django.urls import reverse



# Importando modelos
from .models import AccountModel


# Create your views here.

# Vista para mostrar configuracion 
# del perfil (carga template)
class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = "profile/home.html"

    def get_context_data(self, **kwargs):
             
        obj_user = self.request.user
        obj_account = AccountModel.objects.get(user=obj_user)
        context = super().get_context_data(**kwargs)
        try:
            if not obj_account.image_profile.__bool__():
                context['imagen'] = False

            context['empresa'] = obj_account.business_name
            context['telefono'] = obj_account.telephone
            context['codigo_postal'] = obj_account.postal_code
            context['pais'] = obj_account.country
            context['estado'] = obj_account.state
            context['imagen'] = obj_account.image_profile.url
            
          
        except Exception as ex:
            print(ex)

        return context
    
    def post(self, request, *args, **kwargs):
        response = {}
        try:
            obj_user = request.user
            obj_account = AccountModel.objects.get(user=obj_user)
            if request.FILES.get('imagen'):
                obj_account.image_profile = request.FILES['imagen']

            obj_account.business_name = request.POST.get('empresa', None)
            obj_account.telephone = request.POST.get('telefono', None)
            obj_account.postal_code = request.POST.get('postal', None)
            obj_account.country = request.POST.get('pais', None)
            obj_account.state = request.POST.get('estado', None)
            obj_account.save()
            response['success'] = True    
        except Exception as ex:
            response['success'] = False 
            print(ex)

        return JsonResponse(response)



# Vista para mostrar el formulario 

class RegisterView(LoginRequiredMixin, TemplateView):

    template_name = "profile/form.html"

    def post(self, request, *args, **kwargs):
        response = {}
        try:
            
            print(request.POST.get('rfc'))
            response['success'] = True

        except Exception as ex:
            print(ex)
            response['success'] = False

        
        
        return JsonResponse(response)

    