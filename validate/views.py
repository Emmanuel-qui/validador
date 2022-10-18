
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views import View

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
			m = form.save(commit = False)
			# Obtenemos el file del request y lo amacenamos
			xml_file = m.file

			ext = xml_file.name.split(".")[-1]

			if ext == "xml":
				m.save()
			else:
				return HttpResponse("El archivo no es un documento xml")
       


			# Asignamos nuestra instancia de la clase para validacion, pasandao como argumento el archivo.
			objeto = Validate(xml_file)

			# Regresamos el objeto, con un valor del xml
			print(objeto.success)
			print(objeto.message)

			return HttpResponse(objeto.message)











