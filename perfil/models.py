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
					('615','Régimen de los ingresos por obtención de premios'),
					('616','Sin obligaciones fiscales'),
					('620','Sociedades Cooperativas de Producción que optan por diferir sus ingresos'),
					('621','Incorporación Fiscal'),
					('622','Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'),
					('623','Opcional para Grupos de Sociedades'),
					('624','Coordinados'),
					('625','Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas'),
					('626','Régimen Simplificado de Confianza'),
					]

	pais = [('MX','México')]

	estados =[('AGS','Aguascalientes'),
              ('BC','Baja California'),
              ('BCS','Baja California Sur'),
              ('CAMP','Campeche'),
              ('COAH','Coahuila de Zaragoza'),
              ('COL','Colima'),
              ('CHIS','Chiapas'),
              ('CHIH','Chihuahua'),
              ('DF','Distrito Federal'),
              ('DGO','Durango'),
              ('GTO','Guanajuato'),
              ('GRO','Guerrero'),
              ('HGO','Hidalgo'),
              ('JAL','Jalisco'),
              ('MEX','Estado de México'),
              ('MICH','Michoacán'),
              ('MOR','Morelos'),
              ('NAY','Nayarit'),
              ('NL','Nuevo León'),
              ('OAX','Oaxaca'),
              ('PUE','Puebla'),
              ('QRO','Querétaro'),
              ('QR','Quintana Roo'),
              ('SLP','San Luis Potosí'),
              ('SIN','Sinaloa'),
              ('SON','Sonora'),
              ('TAB','Tabasco'),
              ('TAMS','Tamaulipas'),
              ('TLAX','Tlaxcala'),
              ('VER','Veracruz'),
              ('YUC','Yucatán'),
              ('ZAC','Zacatecas'),
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
	country = models.CharField(max_length=10, choices=pais)

	# estado
	state = models.CharField(max_length=10, choices=estados)

	# codigo postal
	postal_code = models.CharField(max_length=255)

	# regimen fiscal
	regime_fiscal = models.CharField(max_length=10,choices=regimen_fiscal)

	# tipo de persona
	person_type = models.CharField(max_length=1,choices=tipo_persona_choices)

	# imagen 
	image_profile = models.ImageField(upload_to='image/', default='/media/image/img-quadrum.jpeg', null=True, blank=True)