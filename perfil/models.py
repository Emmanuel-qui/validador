from django.db import models

from django.contrib.auth.models import User

#Create your models here.

class AccountModel(models.Model):

	moral = 'M'
	fisica = 'F'

	tipo_persona_choices = [(moral,'Persona Moral'),(fisica, 'Persona Fisica')]

	regimen_fiscal = [('601','General de Ley Personas Morales'),
					('603','Personas Morales con Fines no Lucrativos'),
					('605','Sueldos y Salarios e Ingresos Asimilados a Salarios'),
					('606','Arrendamiento'),
					('607','Régimen de Enajenación o Adquisición de Bienes'),
					('608','Demás ingresos'),
					('610','Residentes en el Extranjero sin Establecimiento Permanente en México'),
					('611','Ingresos por Dividendos (socios y accionistas)'),
					('612','Personas Físicas con Actividades Empresariales y Profesionales'),
					('614','Ingresos por intereses'),
					]

	# relacion con el modelo usuario.
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	# nombre persona
	business_name = models.CharField(max_length=255)
	# rfc
	rfc = models.CharField(max_length=20)

	# telefono
	telephone = models.CharField(max_length=255)

	# pais
	country = models.CharField(max_length=255)

	# estado
	state = models.CharField(max_length=255)

	# codigo postal
	postal_code = models.CharField(max_length=255)

	# regimen fiscal
	regime_fiscal = models.CharField(max_length=10,choices=regimen_fiscal)

	# tipo de persona
	person_type = models.CharField(max_length=1,choices=tipo_persona_choices)

	# imagen 
	image_profile = models.ImageField(upload_to='image/', default='/media/image/img-quadrum.jpeg', null=True, blank=True)