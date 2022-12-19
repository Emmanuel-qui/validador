from django.forms import FileInput, ModelForm

from .models import FileModel


# creacion de formulario para recibir archivos.
class FileForm(ModelForm):
	class Meta:
		model = FileModel
		fields = ['file']
		widgets = {
			"file": FileInput(attrs={'class':'form-control'})
		}
		labels = {
			"file": 'Ingrese el XML a validar'
		}