from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AccountModel


# Create your views here.

# Vista para mostrar configuracion 
# del perfil (carga template)
class ProfileView(LoginRequiredMixin,View):
    login_url = '/accounts/login/'
    def get(self, request):

        obj_user = request.user
        obj_account = AccountModel.objects.get(user=obj_user)
        response = {
            'empresa': obj_account.business_name,
            'telefono': obj_account.telephone,
            'codigo_postal': obj_account.postal_code,
            'pais': obj_account.country,
            'estado': obj_account.state,
            'imagen': obj_account.image_profile

        }
    
        return render(request, 'profile/home.html',context=response)
    
    def post(self, request):
        obj_user = request.user
        obj_account = AccountModel.objects.get(user=obj_user)

        if request.FILES.get('imagen'):
            obj_account.image_profile = request.FILES['imagen']
        
        
        telefono = request.POST['telefono']
        codigo_postal = request.POST['postal']
        pais = request.POST['pais']
        estado = request.POST['estado']
            
        obj_account.business_name = request.POST.get('empresa', None)
        obj_account.telephone = telefono
        obj_account.postal_code = codigo_postal
        obj_account.country = pais
        obj_account.state = estado
        
        obj_account.save()

        response = {'success': True}

        return JsonResponse(response)
    
# Vista para mostrar el formulario 
# de registro de datos.
class RegisterView(LoginRequiredMixin,View):

    def get(self, request):
        
        return render(request, 'profile/form.html')

    def post(self, request):
        
        return JsonResponse('Todo bien')