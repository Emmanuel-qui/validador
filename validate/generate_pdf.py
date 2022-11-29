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
from django.contrib import staticfiles
from reportlab.platypus import Image


class PDF:
    PATH_IMAGE = staticfiles.finders.find("img/img-quadrum.jpeg")
    IMAGE = Image(PATH_IMAGE, width=50, height=50, hAlign='LEFT')
    PRGH_STYLE_HEAD = ParagraphStyle("HEAD", fontSize=16, textColor=colors.HexColor("#7b211f"), alignment=TA_CENTER)
    PRGH_STYLE_HEADER = ParagraphStyle("HEADER", fontSize=14, textColor=colors.white, alignment=TA_CENTER, leading=17)
    PRGH_STYLE_SUBHEADER = ParagraphStyle("SUBHEADER", fontSize=12,textColor=colors.black)
    PRGH_STYLE_CONTENT = ParagraphStyle("CONTENT", fontSize=12,textColor=colors.black, alignment=TA_CENTER, leading=15)
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
        header_data = [Paragraph("<b>Reporte de Validición</b>", self.PRGH_STYLE_HEAD)]
        return header_data

    def get_image(self):
        body_data =[[self.get_header()]]

        body_table = Table(body_data, colWidths=[7*inch, 2*inch], style = [
                ("BACKGROUND",(0,-1), colors.HexColor("#6c757d")),
                ('VALIGN',(0,0),(-1,-1),'TOP'),
            ])

        return body_table

    def get_body(self):
        body_data = [
            [Paragraph("Informacion del Comprobante", self.PRGH_STYLE_HEADER), Paragraph("<b>&nbsp;</b>", self.PRGH_STYLE_HEADER)],
            [Paragraph("Resultado", self.PRGH_STYLE_SUBHEADER), Paragraph(self.results, self.PRGH_STYLE_CONTENT),],
            [Paragraph("RFC Emisor", self.PRGH_STYLE_SUBHEADER), Paragraph(self.rfc_business, self.PRGH_STYLE_CONTENT),],
            [Paragraph("RFC Receptor", self.PRGH_STYLE_SUBHEADER), Paragraph(self.rfc_receiver, self.PRGH_STYLE_CONTENT),],  
            [Paragraph("Fecha", self.PRGH_STYLE_SUBHEADER), Paragraph(self.date, self.PRGH_STYLE_CONTENT),],
            [Paragraph("Version", self.PRGH_STYLE_SUBHEADER), Paragraph(self.version, self.PRGH_STYLE_CONTENT),],
            [Paragraph("Tipo de Comprobante", self.PRGH_STYLE_SUBHEADER), Paragraph(self.voucher_type, self.PRGH_STYLE_CONTENT),],
            [Paragraph("Total", self.PRGH_STYLE_SUBHEADER), Paragraph(self.total, self.PRGH_STYLE_CONTENT),],
            [Paragraph("Subtotal", self.PRGH_STYLE_SUBHEADER), Paragraph(self.subtotal, self.PRGH_STYLE_CONTENT),],
            
        ]
        rowsHeight = [0.3*inch] * len(body_data)
        body_table = Table(body_data, colWidths=[2*inch, 5*inch],rowHeights=rowsHeight, style=[
            ("BACKGROUND",(0,0), (0, 0), colors.HexColor("#7b211f")),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("SPAN", (0, 0), (-1, 0)),
            ("VALIGN", (0, 0), (-1, -1), 'MIDDLE'),
        ])
        return body_table

    def get_body_dos(self):
        body_data = [
            [Paragraph("Resultado de Validación", self.PRGH_STYLE_HEADER), Paragraph("<b>&nbsp;</b>", self.PRGH_STYLE_HEADER)],
            [Paragraph("Fecha de validacion", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.fecha_val), self.PRGH_STYLE_CONTENT),],
            [Paragraph("Sello", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.sell), self.PRGH_STYLE_CONTENT),],
            [Paragraph("Estructura", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.estruc), self.PRGH_STYLE_CONTENT),],
            [Paragraph("Mensaje", self.PRGH_STYLE_SUBHEADER), Paragraph(str(self.error), self.PRGH_STYLE_CONTENT),],
            
        ]

        body_table = Table(body_data,colWidths=[2*inch, 5*inch], style=[
            ("BACKGROUND",(0,0), (0, 0), colors.HexColor("#7b211f")),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("SPAN", (0, 0), (-1, 0)),
            ("VALIGN", (0, 0), (-1, -1), 'TOP'),
        ])
        return body_table
    

    def get_page(canvas, doc):
        canvas.saveState()
        # canvas.setFont('Times-Roman',9)
        canvas.drawString(inch, 0.75 * inch, "Page %d" % (doc.page))
        canvas.restoreState()

    def generate(self):
        result_io = BytesIO()
        doc = SimpleDocTemplate(result_io,title=self.fecha_val, topMargin=0.5*inch, bottomMargin=0.5*inch,)
        story = []
        header = self.get_header()
        story.extend(header)
        story.append(Spacer(0, 14))
        body = self.get_body()
        story.append(body)
        story.append(Spacer(0, 12))
        body_dos = self.get_body_dos()
        story.append(body_dos)
        doc.build(story, onLaterPages=self.get_page)
        return result_io.getvalue()
