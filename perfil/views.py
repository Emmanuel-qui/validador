from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.models import User
from .models import AccountModel

# Create your views here.
class ProfileView(View):

    def get(self, request):
        return render(request, 'profile/home.html')
    
    def post(self, request):
        username = request.user;
        obj_user = User.objects.get(username=username)

        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        rfc = request.POST['rfc']
        codigo_postal = request.POST['postal']
        pais = request.POST['pais']
        estado = request.POST['estado']
        tipo_persona = request.POST['tipo_persona']
        regimen_fiscal = request.POST['regimen_fiscal']
        #email = obj_user.email

        # response = {'nombre': nombre,
        #         'telefono': telefono,
        #         'rfc': rfc,
        #         'codigo': codigo_postal,
        #         'pais': pais,
        #         'estado': estado,
        #         'tipo': tipo_persona,
        #         'regimen': regimen_fiscal,
        #         'email': email
        #         }

        obj_account = AccountModel(obj_user,
            business_name = nombre,
            rfc = rfc,
            telephone = telefono,
            country = pais,
            state = estado,
            postal_code = codigo_postal,
            regime_fiscal = regimen_fiscal,
            person_type = tipo_persona)   

        if obj_account != None:
            obj_account.save()
            data = {'data': obj_account}
            return JsonResponse(data) 

        return JsonResponse('Ocurrio un error')


class UserView(View):

    def get(self, request):

        username = request.user;

        obj_user = User.objects.get(username = username)

        email_user = obj_user.email;

        response = {'email': email_user}

        return JsonResponse(response)