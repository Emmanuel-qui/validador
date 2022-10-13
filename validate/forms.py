from django import forms

from .models import FileModel


# creacion de formulario para recibir archivos.
class FileForm(forms.ModelForm):
	class Meta:
		model = FileModel
		fields = ['file']