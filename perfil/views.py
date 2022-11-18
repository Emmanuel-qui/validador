from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import AccountModel

# Create your views here.

# Vista de configuracion del perfil.
class ProfileView(View):

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
        import pdb; pdb.set_trace()
        obj_user = request.user
        obj_account = AccountModel.objects.get(user=obj_user.id)

        if request.FILES.get('imagen') != None:
            imagen = request.FILES['imagen']
            obj_account.image_profile = imagen
        
        
        empresa = request.POST['empresa']
        telefono = request.POST['telefono']
        codigo_postal = request.POST['postal']
        pais = request.POST['pais']
        estado = request.POST['estado']
            
        obj_account.business_name = empresa
        obj_account.telephone = telefono
        obj_account.postal_code = codigo_postal
        obj_account.country = pais
        obj_account.state = estado
        
        obj_account.save()

        response = {'success': True}

        return JsonResponse(response)
    
# Vista para el formulario de registro.
class RegisterView(View):

    def get(self, request):
        
        return render(request, 'profile/form.html')