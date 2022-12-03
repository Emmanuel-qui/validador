from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import FormView
from .forms import PasswordResetForm, ChangePasswordForm
import smtplib
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

class PasswordResetView(FormView):
    template_name = "registration/password_reset_form.html"
    form_class = PasswordResetForm
    success_url = '/accounts/password_reset/'

    def dispatch(request, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request,*args, **kwargs):
        response = {}
        try:
            form = PasswordResetForm(request.POST)

            if form.is_valid():
                user = form.get_user()
                self.send_email(user)
            else:
                response['error'] = form.errors

        except Exception as ex:
            print(str(ex))


        return JsonResponse(response)


    def send_email(self, user):
        response = {}
        try:
            mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)

            email_to = user.email
            # Construimos el mensaje simple
            mensaje = MIMEMultipart()
            mensaje['From']=settings.EMAIL_HOST_USER
            mensaje['To']=email_to
            mensaje['Subject']="Restablece tu contraseña"

            content = render_to_string('accounts/send_email.html', {'link_resetpwd':'','link_home':''})

            mensaje.attach(MIMEText(content,'html'))

            # Envio del mensaje
            mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())

            print('conectado...')
            print('Correo enviado')
        except Exception as ex:
            response['error'] = str(ex)
            print('ocurrion un error')
            print(ex)


class PasswordChangeView(FormView):
    template_name = "registration/password_change_form.html"
    form_class = ChangePasswordForm