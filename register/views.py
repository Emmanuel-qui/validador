from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
from django.http import JsonResponse
from django_registration.backends.activation.views import ActivationView as BaseActivationView
from django_registration.backends.activation.views import RegistrationView as BaseRegistrationView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings


from django.views.generic.edit import FormView
from .forms import PasswordResetForm, ChangePasswordForm
import smtplib
from django.conf import settings


# Create your views here.
class RegistrationView(BaseRegistrationView):

    def send_activation_email(self, user):
       """
       Send the activation email. The activation key is the username,
       signed using TimestampSigner.

       """
       activation_key = self.get_activation_key(user)
       context = self.get_email_context(activation_key)
       context["user"] = user
       subject = render_to_string(
           template_name=self.email_subject_template,
           context=context,
           request=self.request,
       )
       # Force subject to a single line to avoid header-injection
       # issues.
       subject = "".join(subject.splitlines())
       message = render_to_string(
           template_name=self.email_body_template,
           context=context,
           request=self.request,
       )
       # user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

       send_mail(
           subject,
           '',
           settings.DEFAULT_FROM_EMAIL,
           [user.email],
           html_message=message,
           fail_silently=False,
       )

class ActivationView(BaseActivationView):
    pass

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

            content = render_to_string('send_email.html', {'link_resetpwd':'','link_home':''})

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