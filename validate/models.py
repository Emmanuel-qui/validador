from django.db import models

# Create your models here.

# Modelo para guardar el documento

class FileModel(models.Model):
	
	file = models.FileField(upload_to='documents/')



# Modelo para guardar datos del Documento
class InvoiceModel(models.Model):

	version = models.CharField(max_length = 3)
	series = models.CharField(max_length = 25)
	folio = models.CharField(max_length = 40)
	date = models.CharField(max_length = 19)
	stamp = models.TextField()
	payment_form = models.CharField(max_length = 2)
	no_certificate = models.CharField(max_length = 20)
	certificate = models.TextField()
	payment_conditions = models.TextField()
	rfc_business = models.CharField(max_length = 25)
	name_buiness = models.CharField(max_length = 25)
	rfc_receiver = models.CharField(max_length = 25)
	name_receiver = models.CharField(max_length = 25)
	subtotal = models.CharField(max_length = 255)
	discount = models.CharField(max_length = 255)
	currency = models.CharField(max_length = 3)
	exchange_rate = models.CharField(max_length = 3)
	total = models.CharField(max_length = 255)
	voucher_type = models.CharField(max_length = 1)
	export = models.CharField(max_length = 2)
	forma_pago = models.CharField(max_length = 2)
	place_of_expedition = models.CharField(max_length = 6)
	metodo_pago = models.CharField(max_length = 3)

