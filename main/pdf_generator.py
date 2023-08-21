from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import StockMovement

def generate_pdf_report(queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="stock_movements_report.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(letter))
    elements = []

    # Title and description
    title_style = getSampleStyleSheet()['Title']
    elements.append(Paragraph("Stock Movements Report", title_style))
    elements.append(Spacer(1, 20))

    description_style = getSampleStyleSheet()['Normal']
    description = "This report provides a summary of stock movements for the specified period."
    elements.append(Paragraph(description, description_style))
    elements.append(Spacer(1, 20))

    # Date of the report
    date_style = getSampleStyleSheet()['Normal']
    elements.append(Paragraph("Report Date: 2023-08-21", date_style))
    elements.append(Spacer(1, 40))

    # Table header
    data = [
        ['#', 'Product', 'Movement Type', 'Quantity', 'Total Price (Frw)', 'Date & Time']
    ]
    
    # Initialize row counter
    row_number = 1

    for movement in queryset:
        data.append([
            str(row_number),
            str(movement.product_detail),
            movement.get_movement_type_display(),
            str(movement.quantity),
            str(movement.total_price),
            str(movement.date_time),
        ])
        row_number += 1  # Increment the row counter

    # Table styling
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    return response
