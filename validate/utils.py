from lxml import etree

from pathlib import Path



class Validate:

    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.xml_string = None
        self.xml_string = self.xml_file.read()
        self.xml_etree = None

        self.success = False
        self.message = "Error"

        # funcion que da inicio al proceso de validacion.
        self.start()

    def start(self):
        self.validate_ext()
        if self.success:
            self.validate_xsd()
            if self.success:
                self.validate_ws()

    def validate_xsd(self):
        self.success = False
        try:
            self.xml_etree = etree.fromstring(self.xml_string, settings.INVOICE_XSD_PARSER)

            self.success = True
            self.message = "Estructura valida"
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
        

    def validate_ws(self):
        self.success = False
        pass




