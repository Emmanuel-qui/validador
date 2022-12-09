from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import PasswordResetForm, ChangePasswordForm
import smtplib
from django.conf import settings
from django.template.loader import render_to_string
import uuid


# Create your views here.

# class PasswordResetView(FormView):
#     template_name = "registration/password_reset_form.html"
#     form_class = PasswordResetForm
#     success_url = '/accounts/password_reset/'

#     def dispatch(request, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def post(self, request,*args, **kwargs):
#         response = {}
#         try:
#             form = PasswordResetForm(request.POST)

#             if form.is_valid():
#                 user = form.get_user()
#                 self.send_email(user)
#             else:
#                 response['error'] = form.errors

#         except Exception as ex:
#             print(str(ex))


#         return JsonResponse(response)


#     def send_email(self, user):
#         response = {}
#         try:
#             url = self.request.META['HTTP_HOST']
#             user.token = uuid.uuid4 
#             user.save()
#             mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
#             mailServer.ehlo()
#             mailServer.starttls()
#             mailServer.ehlo()
#             mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)

#             email_to = user.email
#             # Construimos el mensaje simple
#             mensaje = MIMEMultipart()
#             mensaje['From']=settings.EMAIL_HOST_USER
#             mensaje['To']=email_to
#             mensaje['Subject']="Restablece tu contraseña"

#             content = render_to_string('accounts/send_email.html', {
#                 'user': user,
#                 'link_resetpwd':'http://{}/accounts/password_change/{}/'.format(url, str(user.token)),
#                 'link_home':'http://{}'.format(url)})

#             mensaje.attach(MIMEText(content,'html'))

#             # Envio del mensaje
#             mailServer.sendmail(settings.EMAIL_HOST_USER,
#                             email_to,
#                             mensaje.as_string())

#             print('conectado...')
#             print('Correo enviado')
#         except Exception as ex:
#             response['error'] = str(ex)
#             print('ocurrion un error')
#             print(ex)


# class PasswordChangeView(FormView):
#     template_name = "registration/password_change_form.html"
#     form_class = ChangePasswordForm
#     success_url = reverse_lazy(settings.LOGOUT_REDIRECT_URL)

#     def dispatch(self,request, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get(self,request, *args, **kwargs):

#         token = self.kwargs['token']

#         if User.objects.filter(token = token).exists():
#             return super().get(*args, **kwargs)

#         return HttpResponseRedirect(self.success_url)

#     def post(self, request,*args, **kwargs):
#         response = {}
#         try:
#             form = ChangePasswordForm(request.POST)

#             if form.is_valid():
#                 user = User.objects.get(token = self.kwargs['token'])
#                 user.set_password(request.POST['password'])
#                 user.token = uuid.uuid4 
#                 user.save()
#             else:
#                 response['error'] = form.errors

#         except Exception as ex:
#             print(str(ex))


#         return HttpResponseRedirect(self.success_url)