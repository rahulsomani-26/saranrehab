from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_pdf(reg_no, name, address, doj, addiction_type, gender, duration, room_type, monthly_charge, photo_path):
    pdf_path = f"{reg_no}_patient_info.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Set the font and add a title
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    c.setFont("Arial", 14)
    c.drawString(100, 750, f"Registration Number: {reg_no}")
    c.drawString(100, 730, f"Name: {name}")
    c.drawString(100, 710, f"Address: {address}")
    c.drawString(100, 690, f"Date of Joining: {doj}")
    c.drawString(100, 670, f"Addiction Type: {addiction_type}")

    # Add watermark
    c.saveState()
    c.setFillAlpha(0.3)
    c.setFont("Helvetica", 50)
    c.rotate(35)
    c.setFillColor(colors.red)
    c.drawCentredString(400, 400, "SARAN NASHA MUKTI KENDRA")
    c.restoreState()

    # Save the PDF
    c.save()
