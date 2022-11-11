from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class AccountModel(models.Model):

	moral = 'M'
	fisica = 'F'

	tipo_persona_choices = [(moral,'Persona Moral'),(fisica, 'Persona Fisica')]

	# relacion con el modelo usuario.
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# nombre persona
	business_name = models.CharField(max_length=255)

	# telefono
	telephone = models.CharField(max_length=255)

	# pais
	country = models.CharField(max_length=255)

	# estado
	state = models.CharField(max_length=255)

	# codigo postal
	postal_code = models.CharField(max_length=255)

	# regimen fiscal
	regime_fiscal = models.CharField(max_length=255)

	# tipo de persona
	person_type = models.CharField(max_length=1, choices=tipo_persona_choices)

	# imagen 
	image_profile = models.ImageField(upload_to='image-profile/')