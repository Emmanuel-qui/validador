
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views import View

# importando libreria para responder en formato json.
from django.http import JsonResponse


# importando formulario para documentos
from .forms import FileForm

# importamos la clase Validate
from .utils import Validate

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


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
       



class ResultValidate(View):

	def get(self, request):

		return render(request, 'validate/result.html')








