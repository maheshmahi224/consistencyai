# Retry generating the PDF using a fresh approach
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch

# Prepare the data again
data = [
    ["Class", "Subjects"],
    ["1st Class", "Hindi & English"],
    ["2nd Class", "Telugu, E.V.S & Maths"],
    ["3rd Class", "Hindi & English"],
    ["4th Class", "Telugu, E.V.S & Maths"],
    ["5th Class", "Hindi & English"],
    ["6th Class", "Telugu, Maths & Social"],
    ["7th Class", "Hindi, English & Science"],
    ["8th Class", "Telugu, Maths, Physics & Social"],
    ["9th Class", "Hindi, English & Biology"],
    ["10th Class", "Telugu, Maths, Physics & Social"]
]

# Create the PDF file path
pdf_path_retry = "/mnt/data/Weekend_III_Exams_Retry.pdf"

# Set up the document
doc = SimpleDocTemplate(pdf_path_retry, pagesize=A4)
table = Table(data, colWidths=[2.5 * inch, 4 * inch])

# Define the table style
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.Color(1, 0.9, 0.7)),  # Header background
    ('BACKGROUND', (0, 1), (-1, -1), colors.Color(1, 0.97, 0.88)),  # Row background
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # Text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 14),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
]))

# Build the PDF
doc.build([table])

pdf_path_retry
