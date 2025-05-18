from django.db import models

class Fonctionnaire(models.Model):
    nom = models.CharField(max_length=255)
    matricule = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nom} ({self.matricule})"

class BulletinPaie(models.Model):
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    mois = models.CharField(max_length=10)
    annee = models.IntegerField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    fichier_pdf = models.FileField(upload_to='bulletins/')
    date_envoi = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from .utils import generer_pdf_bulletin
        generer_pdf_bulletin(self.fonctionnaire, self)
