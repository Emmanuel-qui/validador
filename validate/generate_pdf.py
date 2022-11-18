from io import BytesIO

from validate.models import ValidateResultModel

from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Spacer
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


class PDF:
    PRGH_STYLE_HEADER = ParagraphStyle("HEADER", fontSize=14, textColor=colors.HexColor("#7b211f"), alignment=TA_CENTER)
    PRGH_STYLE_SUBHEADER = ParagraphStyle("SUBHEADER", fontSize=12,textColor=colors.white)
    PRGH_STYLE_CONTENT = ParagraphStyle("CONTENT", fontSize=12,textColor=colors.black, alignment=TA_CENTER)
    PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
    styles = getSampleStyleSheet()

    def __init__(self, validateresultmodel_id):
        self.validateresultmodel_obj = ValidateResultModel.objects.get(id=validateresultmodel_id)
        self.rfc_receiver = self.validateresultmodel_obj.rfc_receiver
        self.rfc_business = self.validateresultmodel_obj.rfc_business
        self.version = self.validateresultmodel_obj.version
        self.results = self.validateresultmodel_obj.results
        self.voucher_type = self.validateresultmodel_obj.voucher_type
        self.subtotal = self.validateresultmodel_obj.subtotal
        self.total = self.validateresultmodel_obj.total
        self.metodo_pago = self.validateresultmodel_obj.metodo_pago
        self.place_of_expedition = self.validateresultmodel_obj.place_of_expedition
        self.date = self.validateresultmodel_obj.date
        self.validate_date = self.validateresultmodel_obj.validate_date
        self.estruc = self.validateresultmodel_obj.estruc
        self.stamp = self.validateresultmodel_obj.stamp
        self.error = self.validateresultmodel_obj.error_ws
        self.sell = ""
        self.fecha_val = ""
        self.texto()
        
    def texto(self):

        if self.stamp:
            self.sell = "Sello Correcto"
        else:
            self.sell = "Sello Incorrecto"

        self.fecha_val = str(self.validate_date)

        self.fecha_val = self.fecha_val.split(".")

        cadena = ''.join(self.fecha_val)

        self.fecha_val = cadena[0:19]


    def get_header(self):
        header_data = [Paragraph("<b>Informacion del Comprobante</b>", self.PRGH_STYLE_HEADER)]
        return header_data

    def get_body(self):
        body_data = [
            [Paragraph("<b>Resultado</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.results, self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>RFC Emisor</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.rfc_business, self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>RFC Receptor</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.rfc_receiver, self.PRGH_STYLE_CONTENT),],  
            [Paragraph("<b>Fecha</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.date, self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Version</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.version, self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Tipo de Comprobante</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.voucher_type, self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Total</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.total, self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Subtotal</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(self.subtotal, self.PRGH_STYLE_CONTENT),],
            
        ]

        body_table = Table(body_data, colWidths=[2*inch, 5*inch], style=[
            ("BACKGROUND",(0,0), (0, -1), colors.HexColor("#6c757d")),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOX", (0, 0), (-1, -1), 1, colors.black)
        ])
        return body_table

    def get_body_dos(self):
        body_data = [
            [Paragraph("<b>Fecha de validacion</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.fecha_val), self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Sello</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.sell), self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Estructura</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.estruc), self.PRGH_STYLE_CONTENT),],
            [Paragraph("<b>Mensaje</b>", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.error), self.PRGH_STYLE_CONTENT),],
            
        ]

        body_table = Table(body_data,colWidths=[2*inch, 5*inch], style=[
            ("BACKGROUND",(0,0), (0, -1), colors.HexColor("#6c757d")),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOX", (0, 0), (-1, -1), 1, colors.black)
        ])
        return body_table
    
    def get_page(canvas, doc):
        canvas.saveState()
        # canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
        canvas.restoreState()

    def generate(self):
        result_io = BytesIO()
        doc = SimpleDocTemplate(result_io)
        story = []
        header = self.get_header()
        story.extend(header)
        story.append(Spacer(0, 12))
        body = self.get_body()
        story.append(body)
        story.append(Spacer(0, 12))
        body_dos = self.get_body_dos()
        story.append(body_dos)
        doc.build(story, onLaterPages=self.get_page)
        return result_io.getvalue()
