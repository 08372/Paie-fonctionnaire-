from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from django.conf import settings

def generer_pdf_bulletin(fonctionnaire, bulletin):
    filename = f"bulletin_{fonctionnaire.matricule}_{bulletin.mois}_{bulletin.annee}.pdf"
    filepath = os.path.join(settings.BASE_DIR, "media/bulletins", filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "RÉPUBLIQUE DÉMOCRATIQUE DU CONGO")
    c.drawString(100, 780, "Bulletin de Paie")
    c.drawString(100, 750, f"Nom: {fonctionnaire.nom}")
    c.drawString(100, 730, f"Matricule: {fonctionnaire.matricule}")
    c.drawString(100, 710, f"Mois: {bulletin.mois} {bulletin.annee}")
    c.drawString(100, 690, f"Montant: {bulletin.montant} CDF")
    c.drawString(100, 650, "Signature: ___________________")
    c.showPage()
    c.save()

    # Enregistrement dans le modèle (si pas déjà fait)
    bulletin.fichier_pdf.name = f"bulletins/{filename}"
    bulletin.save()