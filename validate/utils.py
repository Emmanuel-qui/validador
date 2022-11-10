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
        #self.xml_string = None
        self.xml_string = self.xml_file.read()
        self.xml_etree = None
        # Datos de la cuenta
        self.username = "jquiroz@finkok.com.mx"
        self.password = "Joseemmanuel_1223"
        self.url = "https://demo-facturacion.finkok.com/servicios/soap/validation.wsdl"

        # diccionario con los mensajes de validacion.
        self.response = {}
        self.success = False
        self.message = "Error"
        self.estruc = False

        # funcion que da inicio al proceso de validacion.
        self.start()

    def start(self):
        self.validate_xsd()
        if self.success:
            self.validate_ws()
            if self.success:
                # Guardamos la informacion
                self.save_invoice()
            
                
      
    # funcion para validar la estructura de los XML.         
    def validate_xsd(self):
        self.success = False
        print("entra a validacion xsd...")
        try:
            self.xml_etree = etree.fromstring(self.xml_string, settings.INVOICE_XSD_PARSER)
            self.success = True
            self.message = "Estructura Valida"
            self.estruc = True
        except Exception as e:
            self.success = True
            self.message = str(e)
            self.estruc = False
            
    # funcion de validacion del ws de finkok
    def validate_ws(self):
        print("validacion ws")
        self.success = False
        lines = "".join(self.xml_file.readlines())
        xml = lines.encode("UTF-8")
        history = HistoryPlugin()
        client = Client(wsdl=self.url, plugins=[history])
        contenido = client.service.validate(self.xml_string, self.username, self.password)
        try:
            error = contenido.error
            if error != None:
                self.response = {'Estructura': self.message,
                            'Sello': str(contenido.sello),
                            'Sello_Sat':str(contenido.sello_sat),
                            'Error': error}
            else:
                error = "¡No existe, ningún error!"
                self.response = {'Estructura': self.message,
                            'Sello': str(contenido.sello),
                            'Sello_Sat':str(contenido.sello_sat),
                            'Error': error}

        except Exception:
            print('Ocurrio una excepcion')
        
        self.success = True
        

      # funcion para guardar datos en el modelo invoice   
    def save_invoice(self):
        self.success = False
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

        estruc = self.response['Estructura'] 
        print(estruc)
        stamp = bool(self.response['Sello'])
        print(stamp)
        stamp_sat = bool(self.response['Sello_Sat'])
        print(stamp_sat)
        error = self.response['Error']
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
        validate_result.save()
        self.success = True
   
    
        

        
        
