from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def render_table_pdf(df, out_path, title="Report"):
    """
    Pandas DataFrame ko ek styled PDF report me convert karta hai.
    """
    # Clean DataFrame -> list of lists
    data = [df.columns.tolist()] + df.fillna("").astype(str).values.tolist()

    # PDF doc setup (Path ko string me convert kiya)
    doc = SimpleDocTemplate(str(out_path), pagesize=A4)
    styles = getSampleStyleSheet()
    elements = [Paragraph(title, styles["Title"]), Spacer(1, 12)]

    # Table banaye
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"✅ PDF generated: {out_path}")
