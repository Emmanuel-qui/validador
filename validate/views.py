
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
			m = form.save()
			# Leemos el xml enviado por el request
			xml_string = m.file.read()

			import pdb; pdb.set_trace()

			print(root)

			# Convertimos nuestro xml en cadena para su manipulacion.
			objeto = Validate(xml_string)

			# Regresamos el objeto, con un valor del xml
			print(objeto)

			return HttpResponse('Exitoso')











