from lxml import etree
from zeep import Client
from lxml import etree
from zeep.plugins import HistoryPlugin
from django.conf import settings

# Importamos modelo.
from .models import InvoiceModel, ValidateResultModel


class Validate:

    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.xml_string = self.xml_file.read()

        # Datos de la cuenta
        self.username = settings.USERNAME
        self.password = settings.PASSWORD
        self.url = settings.URL_WS        
        # diccionario con los mensajes de validacion.
        self.response = {}

        # funcion que da inicio al proceso de validacion.
        self.start()

    def start(self):
        self.validate_ws()

  
            
    
            
    # funcion de validacion del ws de finkok
    def validate_ws(self):
        history = HistoryPlugin()
        client = Client(wsdl=self.url, plugins=[history])
        contenido = client.service.validate(self.xml_string, self.username, self.password)
        try:
            error = contenido.error
            if error != None:
                self.response['Estructura'] = "Estructura invalida"
                self.response['Sello'] = contenido.sello
                self.response['Sello_Sat'] = contenido.sello_sat
                self.response['Error'] = error
            else:
                error = "¡No existe, ningún error!"
                self.response['Estructura'] = "Estructura valida"
                self.response['Sello'] = contenido.sello
                self.response['Sello_Sat'] = contenido.sello_sat
                self.response['Error'] = error
            

            self.save_invoice()
        except Exception as e:
            print(e)
        
        

      # funcion para guardar datos en el modelo invoice   
    def save_invoice(self):
        
        voucher = etree.fromstring(self.xml_string)
        namespace = {'cfdi':"http://www.sat.gob.mx/cfd/4"}

        version = voucher.xpath('string(./@Version)',namespaces = namespace)
        serie = voucher.xpath('string(./@Serie)',namespaces = namespace)
        folio = voucher.xpath('string(./@Folio)',namespaces = namespace)
        fecha = voucher.xpath('string(./@Fecha)',namespaces = namespace)
        sello = voucher.xpath('string(./@Sello)',namespaces = namespace)
        formapago = voucher.xpath('string(./@FormaPago)',namespaces = namespace)
        nocertificado = voucher.xpath('string(./@NoCertificado)',namespaces = namespace)
        certificado = voucher.xpath('string(./@Certificado)',namespaces = namespace)
        condicionespago = voucher.xpath('string(./@CondicionesDePago)',namespaces = namespace)

        subtotal = voucher.xpath('string(./@SubTotal)',namespaces = namespace)
        descuento = voucher.xpath('string(./@Descuento)',namespaces = namespace)
        moneda = voucher.xpath('string(./@Moneda)',namespaces = namespace)
        tipocambio = voucher.xpath('string(./@TipoCambio)',namespaces = namespace)
        total = voucher.xpath('string(./@Total)',namespaces = namespace)
        tipocomprobante = voucher.xpath('string(./@TipoDeComprobante)',namespaces = namespace)
        exportacion = voucher.xpath('string(./@Exportacion)',namespaces = namespace)
        lugarexpedicion = voucher.xpath('string(./@LugarExpedicion)',namespaces = namespace)
        metodopago = voucher.xpath('string(./@MetodoPago)',namespaces = namespace)

        # datos del emisor
        emisor = voucher.xpath('.//cfdi:Emisor', namespaces = namespace)[0]
        
        rfc_emisor = emisor.xpath('string(./@Rfc)',namespaces = namespace)
        nombre_emisor = emisor.xpath('string(./@Nombre)',namespaces = namespace)
        
        

        # datos del receptor
        receptor = voucher.xpath('.//cfdi:Receptor', namespaces = namespace)[0]
        rfc_receptor = receptor.xpath('string(./@Rfc)',namespaces = namespace)
        nombre_receptor = receptor.xpath('string(./@Nombre)',namespaces = namespace)

        try:
            invoice = InvoiceModel(version = version,
                                series = serie,
                                folio = folio,
                                date = fecha,
                                stamp = sello,
                                payment_form = formapago,
                                no_certificate = nocertificado,
                                certificate = certificado,
                                payment_conditions = condicionespago,
                                rfc_business = rfc_emisor,
                                name_business = nombre_emisor,
                                rfc_receiver = rfc_receptor,
                                name_receiver = nombre_receptor,
                                subtotal =subtotal,
                                discount = descuento,
                                currency = moneda,
                                exchange_rate = tipocambio,
                                total = total,
                                voucher_type = tipocomprobante,
                                export = exportacion,
                                place_of_expedition = lugarexpedicion,
                                metodo_pago = metodopago
                            )
            
            invoice.save()
            print(self.getValue(tipocomprobante).get('tipo'))
            print(self.response.get('Estructura'))
            print(self.getValue(tipocomprobante).get('sello'))
            print(self.getValue(tipocomprobante).get('sello_sat'))
            print(self.response.get('Error'))

            validate_result = ValidateResultModel(
                                            invoice = invoice,
	                                        voucher_type = self.getValue(tipocomprobante).get('tipo'),
	                                        version = version,
	                                        rfc_business = rfc_emisor,
	                                        rfc_receiver = rfc_receptor,
	                                        subtotal = subtotal,
	                                        total = total, 
	                                        metodo_pago = metodopago,
	                                        place_of_expedition = lugarexpedicion, 
	                                        date = fecha,
                                            estruc = self.response.get('Estructura'), 
	                                        stamp = self.getValue(tipocomprobante).get('sello'),
                                            stamp_sat = self.getValue(tipocomprobante).get('sello_sat'),
                                            error_ws = self.response.get('Error'),
                                            )
        
            validate_result.save()
        except Exception as ex:
            print(ex)
        

    def getValue(self, tipocomprobante):

        data = {}
    
        stamp = bool(self.response.get('Sello'))
        stamp_sat = bool(self.response.get('Sello_Sat'))
        
        if tipocomprobante == "I":
            data['tipo'] = "Ingreso"
        elif tipocomprobante == "E":
            data['tipo'] = "Egreso"
        elif tipocomprobante == "N":
            data['tipo'] = "Nomina"
        elif tipocomprobante == "T":
            data['tipo'] = "Traslado"
        else:
            data['tipo'] = tipocomprobante

        data['sello_sat'] = "No encontrado"
        if stamp_sat:
            data['sello_sat'] = "Encontrado"

        data['sello'] = "Incorrecto"
        if stamp:
            data['sello'] = "Correcto"
        

        return data
        
        
        
   
    
        

        
        
