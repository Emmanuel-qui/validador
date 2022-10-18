from lxml import etree




class Validate:

	def __init__(self,xml_string):
		self.xml_string = xml_string
		#root = etree.fromstring(xml_string)
		
		XSD_PATH = str(Path(BASE_DIR, '/validate/xsd/'))
		INVOICE_XSD_NAME = '/validate/xsd/cfdv40.xsd'
		INVOICE_XSD_FILE = Path(BASE_DIR, INVOICE_XSD_NAME)

		if INVOICE_XSD_FILE.exists():
    		INVOICE_XSD_STRING = INVOICE_XSD_FILE.read_bytes()
    		INVOICE_XSD_STRING = INVOICE_XSD_STRING.decode()
    		INVOICE_XSD_SCHEMA_ROOT = etree.XML(INVOICE_XSD_STRING)
    		INVOICE_XSD_SCHEMA = etree.XMLSchema(INVOICE_XSD_SCHEMA_ROOT)
    		INVOICE_XSD_PARSER = etree.XMLParser(schema=INVOICE_XSD_SCHEMA)
			
			
		return print(root = etree.fromstring(xml_string, INVOICE_XSD_PARSER)

		



