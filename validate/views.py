
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views import View

# importando formulario para documentos
from .forms import FileForm


# Create your views here.

class IndexView(View):

	def get(self, request):
		#Obtenemos el formulario creado y lo mandamos a la vista.
		form = FileForm()

		return render(request, 'validate/index.html', {'form':form})

	def post(self, request):
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print(request.FILES['file'])

			return HttpResponse('Enviado')

