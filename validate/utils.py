from lxml import etree
from zeep import Client
from lxml import etree
from zeep.plugins import HistoryPlugin
from django.conf import settings

# Importamos modelo.
from .models import InvoiceModel


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
        self.save = False

        # funcion que da inicio al proceso de validacion.
        self.start()

    def start(self):
        self.validate_xsd()
        if self.success:
            self.validate_ws()
            if self.save:
                self.save_invoice()
                    
       
                
        
      
    # funcion para validar la estructura de los XML.         
    def validate_xsd(self):
        self.success = False
        print("entra a validacion xsd...")
        try:
            self.xml_etree = etree.fromstring(self.xml_string, settings.INVOICE_XSD_PARSER)
            self.success = True
            self.message = "Estructura valida XSD"
            self.save = True
        except Exception as e:
            self.success = True
            self.message = str(e)
            self.save = False
          
            

    # funcion para validar que sea un archivo xml
    def validate_ext(self):
        ext = self.xml_file.name.split(".")[-1]
        if ext.lower() == "xml":
            self.xml_string = self.xml_file.read()
            self.success = True
            self.message = "extencion valida"
        elif ext.upper() == "XML":
            self.xml_string = self.xml_file.read()
            self.success = True
            self.message = "extencion valida"
        else:
            self.message = "El archivo no es un documento XML"

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
            self.response = {'Estructura': self.message,
                            'Sello': str(contenido.sello),
                            'Sello_Sat':str(contenido.sello_sat),
                            'Error': error}
        except Exception:
            print(contenido.sat)
            print(contenido.sat.Estado)
            print(contenido.sat.CodigoEstatus)
        
        self.success = True
        

      # funcion para guardar datos en el modelo invoice   
    def save_invoice(self):
        self.success = False
        voucher = etree.fromstring(self.xml_string)
        namespace = {'cfdi':"http://www.sat.gob.mx/cfd/4"}

        version = voucher.get('Version')
        serie = voucher.get('Serie')
        folio = voucher.get('Folio')
        fecha = voucher.get('Fecha')
        sello = voucher.get('Sello')
        formapago = voucher.get('FormaPago')
        nocertificado = voucher.get('NoCertificado')
        certificado = voucher.get('Certificado')
        condicionespago = voucher.get('CondicionesDePago')
        # datos del e y r
        subtotal = voucher.get('SubTotal')
        descuento = voucher.get('Descuento')
        moneda = voucher.get('Moneda')
        tipocambio = voucher.get('TipoCambio')
        total = voucher.get('Total')
        tipocomprobante = voucher.get('TipoDeComprobante')
        exportacion = voucher.get('Exportacion')
        lugarexpedicion = voucher.get('LugarExpedicion')
        metodopago = voucher.get('MetodoPago')

        # datos del emisor
        emisor = voucher.xpath('.//cfdi:Emisor', namespaces = namespace)[0]
        rfc_emisor = emisor.get('Rfc')
        nombre_emisor = emisor.get('Nombre')
        

        # datos del receptor
        receptor = voucher.xpath('.//cfdi:Emisor', namespaces = namespace)[0]
        rfc_receptor = receptor.get('Rfc')
        nombre_receptor = receptor.get('Nombre')
        
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
        self.success = True



        
