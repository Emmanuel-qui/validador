# Importanciones Django.
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import View

from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from django.template.loader import render_to_string


# importando formulario para documentos
from .forms import FileForm

# importamos clases de app Validate
from .utils import Validate
from .generate_pdf import PDF

# Importamos el modelo
from .models import ValidateResultModel

from django.conf import settings




# Vista principal validate
class IndexView(LoginRequiredMixin, FormView):
    
    template_name = 'validate/index.html'
    form_class = FileForm

    def post(self, request, *args, **kwargs):
        try:
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                m = form.save()
            # Obtenemos el file del request y lo amacenamos
                xml_file = m.file
            # mandamos el xml como parametro a la clase Validate para hacer el proceso de validacion.
                validate = Validate(xml_file)
                print(validate.response)
                
        except Exception as ex:
            print(ex)


        return JsonResponse(validate.response)
        
        

# Vista de Resultado.
class ResultValidate(LoginRequiredMixin, TemplateView):

    template_name = "validate/result.html"

    def post(self, request, *args, **kwargs):

        response = {}
        try:
            lista_result = []
            start = int(request.POST.get('start'))
            length = int(request.POST.get('length'))

            rfc_emisor = request.POST.get('rfc_emisor')
            rfc_receptor = request.POST.get('rfc_receptor')
            fecha_validate = request.POST.get('fecha_validacion')

            lista_objetos = ValidateResultModel.objects.all()

            if rfc_emisor:
                lista_objetos = lista_objetos.filter(rfc_business__icontains=rfc_emisor)
            elif rfc_receptor:
                lista_objetos = lista_objetos.filter(rfc_receiver__icontains=rfc_receptor)
            elif fecha_validate:
                lista_objetos = lista_objetos.filter(validate_date__icontains=fecha_validate)
            
            total_records = lista_objetos.count()
            lista_objetos = lista_objetos[start:start+length]

            for item in lista_objetos:
                lista_result.append({
                    'id': item.id,
                    'rfc_emisor': item.rfc_business,
                    'rfc_receptor': item.rfc_receiver,
                    'version': item.version,
                    'fecha': item.date,
                    'fecha_validacion':item.validate_date,
                    'sello':item.stamp,
                })

            response = {
                "aaData": lista_result,
                "iTotalRecords": total_records,
                "iTotalDisplayRecords": total_records,
            }
            
        except Exception as ex:
            print(ex)
        
        return JsonResponse(response)

        
# Vista para el detalle
class DetailView(LoginRequiredMixin, TemplateView):

    template_name = 'validate/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            validate_invoice = ValidateResultModel.objects.get(id=kwargs['pk'])

            context['id'] = validate_invoice.id
            context['Version'] = validate_invoice.version
            context['Receptor'] = validate_invoice.rfc_receiver
            context['Metodo_pago'] = validate_invoice.metodo_pago
            context['Emisor'] = validate_invoice.rfc_business
            context['Fecha'] = validate_invoice.date
            context['Fecha_validacion'] = validate_invoice.validate_date
            context['Lugar_ex'] = validate_invoice.place_of_expedition
            context['Tipo'] = validate_invoice.voucher_type
            context['Subtotal'] = validate_invoice.subtotal
            context['Total'] = validate_invoice.total
            context['Estructura'] = validate_invoice.estruc
            context['Sello'] = validate_invoice.stamp
            context['Sello_sat'] = validate_invoice.stamp_sat
            context['Error_msj'] = validate_invoice.error_ws
        except Exception as ex:
            print(ex)
        return context		



    
# Vista generacion de PDF.
class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        try:
            pdf_obj = PDF(kwargs['pk'])
            pdf_result = pdf_obj.generate()
            response = HttpResponse(pdf_result, content_type='application/pdf')
        except Exception as ex:
            print(ex)
        
        return response



# Vista para el envio de Email
class UserEmail(View):

    def get(self, request, *args, **kwargs):
        response = {}
        try:
            user_obj = request.user
            pdf_obj = PDF(kwargs['pk'])
            obj_validate = ValidateResultModel.objects.get(id=kwargs['pk'])
            pdf_result = pdf_obj.generate()

            content = render_to_string(
                "validate/send_email.html", {'user': user_obj.username, 'fecha': str(obj_validate.validate_date)})

            msj = EmailMessage(subject="Reporte de Comprobante",
                               from_email=settings.EMAIL_HOST_USER,
                               to=[user_obj.email],
                               )
            msj.attach(MIMEText(content, 'html'))

            msj.attach('reporte.pdf', pdf_result, 'application/pdf')

            msj.send()

            response['success'] = True
            response['email'] = user_obj.email    
        except Exception as ex:
            response['success'] = False
            print(str(ex))

        return JsonResponse(response)
