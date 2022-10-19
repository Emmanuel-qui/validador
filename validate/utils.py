import re
from lxml import etree

from pathlib import Path

from zeep import Client
import logging
import base64
from lxml import etree
from zeep.plugins import HistoryPlugin


from django.conf import settings




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

        self.lista_errores = []
        



        self.success = False
        self.message = "Error"

        # funcion que da inicio al proceso de validacion.
        self.start()

    def start(self):
        self.validate_ws()
       
                
        
      
            

    def validate_xsd(self):
        self.success = False
        print("entra a validacion xsd")
        try:
            self.xml_etree = etree.fromstring(self.xml_string, settings.INVOICE_XSD_PARSER)

            self.success = True
            self.message = "Estructura valida"
            self.lista_errores.append(self.message)
        except Exception as e:
            self.message = str(e)

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
        contenido = client.service.validate(xml, self.username, self.password)
        print(contenido)
        

        try:
            error = contenido.error
            self.message = error
        except Exception:
            self.lista_errores.append(self.message)
            self.lista_errores.append(str(contenido.xml))
            self.lista_errores.append(str(contenido.sello))
            self.lista_errores.append(str(contenido.sello_sat))
            self.lista_errores.append(str(contenido.sat.Estado))
            self.lista_errores.append(str(contenido.sat.CodigoEstatus))

            mensaje = ",".join(self.lista_errores)
            self.success = True

            self.message = mensaje
        

        request = etree.tostring(history.last_sent["envelope"])
        request = request.decode("UTF-8") 
        self.lista_errores.append(request)

        response = etree.tostring(history.last_received["envelope"])
        response = response.decode("UTF-8") 
        self.lista_errores.append(response)
        mensaje = ",".join(self.lista_errores)
        self.success = True

        self.message = mensaje

        
