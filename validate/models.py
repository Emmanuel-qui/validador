from django.db import models

# Create your models here.

# Modelo para guardar el documento

class FileModel(models.Model):
	
	file = models.FileField(upload_to='documents/')

# Modelo para guardar datos del Documento
class InvoiceModel(models.Model):
	version = models.CharField(max_length = 25, default='No encontrado')
	series = models.CharField(max_length = 255, default='No encontrado')
	folio = models.CharField(max_length = 50, default='No encontrado')
	# fecha
	date = models.CharField(max_length = 25, default='No encontrado')
	# sello
	stamp = models.TextField(default='No encontrado')
	# forma_pago
	payment_form = models.CharField(max_length = 25, default='No encontrado')
	no_certificate = models.CharField(max_length = 25, default='No encontrado')
	certificate = models.TextField(default='No encontrado')
	# condiciones_pago
	payment_conditions = models.TextField(default='No encontrado')
	rfc_business = models.CharField(max_length = 25, default='No encontrado')
	name_business = models.CharField(max_length = 255, default='No encontrado')
	rfc_receiver = models.CharField(max_length = 25, default='No encontrado')
	name_receiver = models.CharField(max_length = 255, default='No encontrado')
	subtotal = models.CharField(max_length = 255, default='No encontrado')
	#descuento
	discount = models.CharField(max_length = 255, default='No encontrado')
	# moneda
	currency = models.CharField(max_length = 25, default='No encontrado')
	#tipo_cambio
	exchange_rate = models.CharField(max_length = 25, default='No encontrado')

	total = models.CharField(max_length = 255, default='No encontrado')
	# tipodecomprobante
	voucher_type = models.CharField(max_length = 25, default='No encontrado')
	# exportacion
	export = models.CharField(max_length = 25, default='No encontrado')
	# luga_expedicion
	place_of_expedition = models.CharField(max_length = 25, default='No encontrado')

	metodo_pago = models.CharField(max_length = 25, default='No encontrado')

 # modelo para guardar el resultado.
class ValidateResultModel(models.Model):
	invoice = models.OneToOneField(InvoiceModel, on_delete = models.CASCADE)
	# tipodecomprobante
	voucher_type = models.CharField(max_length = 255, null = False)
	# version
	version = models.CharField(max_length = 255, null=False)
	# rfc_emisor
	rfc_business = models.CharField(max_length = 255, null=False)
	# rfc_receptor
	rfc_receiver = models.CharField(max_length = 255, null=False)
	# subtotal
	subtotal = models.CharField(max_length = 255, null=False)
	# total
	total = models.CharField(max_length = 255, null = False)
	# metodo_pago
	metodo_pago = models.CharField(max_length = 255, null = True)
	# luga_expedicion
	place_of_expedition = models.CharField(max_length = 255, null = False)
	# fecha
	date = models.CharField(max_length = 255, null=False)
	# fecha_validacion
	validate_date = models.DateField(auto_now= True)
	# estructura
	estruc = models.CharField(max_length = 255, null = True)
	# sello
	stamp = models.CharField(max_length=255,null = True)
	#sello_sat
	stamp_sat = models.CharField(max_length=255,null = True)
	# error del ws
	error_ws = models.TextField(null=True)



