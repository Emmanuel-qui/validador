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
        self.xml_etree = None
        # Datos de la cuenta
        self.username = settings.USERNAME
        self.password = settings.PASSWORD
        self.url = settings.URL_WS        
        # diccionario con los mensajes de validacion.
        self.response = {}
        self.success = False
        self.estruc = False
        self.message = ''

        # funcion que da inicio al proceso de validacion.
        self.start()

    def start(self):
        if self.validate_xsd():
            self.response['success'] = True
            print(self.validate_xsd())
            self.validate_ws()

            if self.validate_ws():
                self.save_invoice()

        else:
            self.response['success'] = False

  
            
        
            
                
      
    # funcion para validar la estructura de los XML.         
    def validate_xsd(self):
        bandera = False
    
        try:
            self.xml_etree = etree.fromstring(self.xml_string, settings.INVOICE_XSD_PARSER)

            bandera = True
            self.message = 'Estructura Valida'

        except Exception as e:
            self.message = 'Estructura Invalida'

            print('Error')
            print(e)
            self.response['msj'] = str(e)
        

        return bandera
            
    # funcion de validacion del ws de finkok
    def validate_ws(self):
        bandera = False

        lines = "".join(self.xml_file.readlines())
        xml = lines.encode("UTF-8")
        history = HistoryPlugin()
        client = Client(wsdl=self.url, plugins=[history])
        contenido = client.service.validate(self.xml_string, self.username, self.password)
        try:
            error = contenido.error
            if error != None:
                self.response['Estructura'] = self.message
                self.response['Sello'] = contenido.sello
                self.response['Sello_Sat'] = contenido.sello_sat
                self.response['Error'] = error


               # self.response = {'Estructura': self.message,
                #            'Sello': str(contenido.sello),
                #            'Sello_Sat':str(contenido.sello_sat),
                #            'Error': error}
            else:
                error = "¡No existe, ningún error!"
                self.response['Estructura'] = self.message
                self.response['Sello'] = contenido.sello
                self.response['Sello_Sat'] = contenido.sello_sat
                self.response['Error'] = error
                self.estruc = True
            bandera = True

        except Exception as e:
            print(e)
        

        return bandera
        

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
        # datos del e y r
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

        estruc = self.response.get('Estructura') 
        print(estruc)
        stamp = bool(self.response.get('Sello'))
        print(stamp)
        stamp_sat = bool(self.response.get('Sello_Sat'))
        print(stamp_sat)
        error = self.response.get('Error')
        print(error)


        resultado = ""
        if self.estruc:
            resultado = "Comprobante Valido"
        else:
            resultado = "Comprobante Invalido"

        
        validate_result = ValidateResultModel(
                                            invoice = invoice, 
	                                        results = resultado,
	                                        voucher_type = tipocomprobante,
	                                        version = version,
	                                        rfc_business = rfc_emisor,
	                                        rfc_receiver = rfc_receptor,
	                                        subtotal = subtotal,
	                                        total = total, 
	                                        metodo_pago = metodopago,
	                                        place_of_expedition = lugarexpedicion, 
	                                        date = fecha,
                                            estruc = estruc, 
	                                        stamp = stamp,
                                            stamp_sat = stamp_sat,
                                            error_ws = error,
                                            )
        print(self.response)
        validate_result.save()
        
   
    
        

        
        
