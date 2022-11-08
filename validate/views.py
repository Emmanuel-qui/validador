from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views import View
# importando libreria para responder en formato json.
from django.http import JsonResponse
# importando formulario para documentos
from .forms import FileForm
# importamos la clase Validate
from .utils import Validate
# Importamos el modelo
from .models import ValidateResultModel
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Librerias para la creacion del PDF
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4





# Create your views here.

class IndexView(View):

	def get(self, request):
		#Obtenemos el formulario creado y lo mandamos a la vista.
		form = FileForm()

		return render(request, 'validate/index.html', {'form':form})

	def post(self, request):
		# Obtenemos el documento enviado
		form = FileForm(request.POST, request.FILES)
		
		if form.is_valid():
			m = form.save()
			# Obtenemos el file del request y lo amacenamos
			xml_file = m.file
			# mandamos el xml como parametro a la clase Validate para hacer el proceso de validacion.
			validate = Validate(xml_file)
			print(validate.response)
			return JsonResponse(validate.response)
       


# Cargando la vista
class ResultValidate(View):

	template_name = "validate/result.html"

	def get(self, request):
		return render(request, self.template_name)


# vista para la logica 
class ValidateResult(View):

	def post(self, request):
		lista_result = []
		start = int(request.POST.get("start"))
		length = int(request.POST.get("length"))
		rfc_emisor = request.POST.get("rfc_emisor")
		rfc_receptor = request.POST.get("rfc_receptor")
		fecha_validate = request.POST.get("fecha_validacion")

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
			"iTotalDisplayRecords": len(lista_objetos),
		}
		return JsonResponse(response)




# funcion del detalle de la validacion

def ValidateResultDetail(request, pk):

	validate_invoice = ValidateResultModel.objects.get(id=pk)

	return render(request, 'validate/detail.html', {'validate_invoice': validate_invoice})

	

# Vista para la generacion de PDF.

class GeneratePdf(View):

	def get(self, request, pk):

		
		response = HttpResponse(content_type='application/pdf')
		
		return response
