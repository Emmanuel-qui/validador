from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import AccountModel

# Create your views here.
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
        # import pdb; pdb.set_trace()

        print(request.POST)
        print(request.FILES)

        if request.POST['imagen'] == "undefined":
            print('entra')
            obj_user = request.user
            obj_account = AccountModel.objects.get(user=obj_user.id)

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

        else:
            print('entra2')
            obj_user = request.user
            obj_account = AccountModel.objects.get(user=obj_user.id)

            empresa = request.POST['empresa']
            telefono = request.POST['telefono']
            codigo_postal = request.POST['postal']
            pais = request.POST['pais']
            estado = request.POST['estado']
            imagen = request.FILES['imagen']

            obj_account.business_name = empresa
            obj_account.telephone = telefono
            obj_account.postal_code = codigo_postal
            obj_account.country = pais
            obj_account.state = estado
            obj_account.image_profile = imagen
            
            
        
        
        obj_account.save()

        response = {'success': True}

        return JsonResponse(response)
        # username = request.user;
        # obj_user = User.objects.get(username=username)

        # nombre = request.POST['nombre']
        # telefono = request.POST['telefono']
        # rfc = request.POST['rfc']
        # codigo_postal = request.POST['postal']
        # pais = request.POST['pais']
        # estado = request.POST['estado']
        # tipo_persona = request.POST['tipo_persona']
        # regimen_fiscal = request.POST['regimen_fiscal']
        # #email = obj_user.email

        # # response = {'nombre': nombre,
        # #         'telefono': telefono,
        # #         'rfc': rfc,
        # #         'codigo': codigo_postal,
        # #         'pais': pais,
        # #         'estado': estado,
        # #         'tipo': tipo_persona,
        # #         'regimen': regimen_fiscal,
        # #         'email': email
        # #         }

        # obj_account = AccountModel(user = obj_user,
        #     business_name = nombre,
        #     rfc = rfc,
        #     telephone = telefono,
        #     country = pais,
        #     state = estado,
        #     postal_code = codigo_postal,
        #     regime_fiscal = regimen_fiscal,
        #     person_type = tipo_persona,
        #     image_profile = None)

        # obj_account.save()   

        # return JsonResponse('Registro exitoso')

# Obtencion de datos de la cuenta
class UserView(View):

    def get(self, request):
        username = request.user;
        obj_user = User.objects.get(username = username)
        obj_account = AccountModel.objects.get(user=obj_user)

        email_user = obj_user.email;
        name_account = obj_account.business_name;

        response = {'email': email_user, 
                    'name': name_account
                    }

        return JsonResponse(response)


class DataUserView(View):

    def get(self, request):
        username = request.user;
        obj_user = User.objects.get(username = username)
        obj_account = AccountModel.objects.get(user=obj_user)
        response = {
            'telefono': obj_account.telephone,
            'codigo_postal': obj_account.postal_code,
            'pais': obj_account.country,
            'estado': obj_account.state,

        }

        print(response)
    
        return JsonResponse(response)

    def post(self, request):
        username = request.user;
        obj_user = User.objects.get(username=username)
        obj_account = AccountModel.objects.get(user=obj_user)
        telefono = request.POST['telefono']
        codigo_postal = request.POST['postal']
        pais = request.POST['pais']
        estado = request.POST['estado']

        update_obj_account = AccountModel(user = obj_user,
            business_name = obj_account.business_name,
            rfc = obj_account.rfc,
            telephone = telefono,
            country = pais,
            state = estado,
            postal_code = codigo_postal,
            regime_fiscal = obj_account.regime_fiscal,
            person_type = obj_account.person_type,
            image_profile = None)
        
        update_obj_account.save()

        return JsonResponse('Actualizacion correcta')