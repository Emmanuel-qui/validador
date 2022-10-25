from django.db import models

# Create your models here.

# Modelo para guardar el documento

class FileModel(models.Model):
	
	file = models.FileField(upload_to='documents/')


# Modelo para guardar datos del Documento
class InvoiceModel(models.Model):
	version = models.CharField(max_length = 3, null=False)
	series = models.CharField(max_length = 25, null = True)
	folio = models.CharField(max_length = 40, null = True)
	# fecha
	date = models.CharField(max_length = 20, null=False)
	# sello
	stamp = models.TextField(null=False)
	# forma_pago
	payment_form = models.CharField(max_length = 2, null = True)
	no_certificate = models.CharField(max_length = 20, null=False)
	certificate = models.TextField(null = False)
	# condiciones_pago
	payment_conditions = models.TextField(null = True)
	rfc_business = models.CharField(max_length = 25, null=False)
	name_business = models.CharField(max_length = 25, null=False)
	rfc_receiver = models.CharField(max_length = 25, null=False)
	name_receiver = models.CharField(max_length = 25, null=False)
	subtotal = models.CharField(max_length = 255, null=False)
	#descuento
	discount = models.CharField(max_length = 255, null = True)
	# moneda
	currency = models.CharField(max_length = 3, null=False)
	#tipo_cambio
	exchange_rate = models.CharField(max_length = 3, blank = True)

	total = models.CharField(max_length = 255, null = False)
	# tipodecomprobante
	voucher_type = models.CharField(max_length = 1, null = False)
	# exportacion
	export = models.CharField(max_length = 2, null = False)
	# luga_expedicion
	place_of_expedition = models.CharField(max_length = 6, null = False)

	metodo_pago = models.CharField(max_length = 3, null = True)

 # modelo para guardar el resultado.
class ValidateResultModel(models.Model):
	invoice = models.OneToOneField(InvoiceModel, on_delete = models.CASCADE)
	results = models.CharField(max_length = 255, null = False)
	# tipodecomprobante
	voucher_type = models.CharField(max_length = 1, null = False)
	# version
	version = models.CharField(max_length = 3, null=False)
	# rfc_emisor
	rfc_business = models.CharField(max_length = 25, null=False)
	# rfc_receptor
	rfc_receiver = models.CharField(max_length = 25, null=False)
	# subtotal
	subtotal = models.CharField(max_length = 255, null=False)
	# total
	total = models.CharField(max_length = 255, null = False)
	# metodo_pago
	metodo_pago = models.CharField(max_length = 3, null = True)
	# luga_expedicion
	place_of_expedition = models.CharField(max_length = 6, null = False)
	# fecha
	date = models.CharField(max_length = 20, null=False)
	# fecha_validacion
	validate_date = models.DateTimeField(auto_now = True)
	# sello
	stamp = models.BooleanField(null = False)


