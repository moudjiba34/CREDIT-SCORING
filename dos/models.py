from django.db import models
from dos.script_one_client import predict


# Create your models here.

class Dos(models.Model):

    status_garantie = (
        ('False', 'False'),
        ('True', 'True')
    )

    type_compte = (
        ('Physique', 'Physique'),
        ('moral', 'moral'),
        ('Autre', 'Autre')
    )

    statut_compte = (
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif')

    )
    statut_remboursement = (
        ('mensuel', 'mensuel'),
        ('trimestriel', 'trimestriel')
    )
    motif_pret = (
        ('acqui', 'acqui'),
        ('const', 'const'),
        ('cons', 'cons'),

    )
    type_identification = (
        ('Carte identité nationale', 'Carte identité nationale'),
        ('Passeport', 'Passeport'),
        ('Certificat de naissance', 'Certificat de naissance'),
        ('Permis de conduire', 'Permis de conduire'),
        ('Titre de séjour', 'Titre de séjour'),
        ('NINEA et RC', 'NINEA ET RC'),
        ('Autre', 'Autre')
    )



    type_pret = models.CharField(max_length=250, choices=motif_pret)
    numero_compte = models.CharField(max_length=250)
    type_client = models.CharField(max_length=250, choices=type_compte)
    montant_pret = models.FloatField()
    taux_interet = models.CharField(max_length=10)
    viln = models.CharField(max_length=250)
    date_ouverture = models.DateField()
    date_naissance = models.DateField()
    statut_compte = models.CharField(max_length=250, choices=statut_compte)
    autre_garantie = models.CharField(max_length=10, choices=status_garantie)
    duree_remboursement = models.CharField(max_length=10)
    rythme_remboursement = models.CharField(max_length=10, choices=statut_remboursement)
    Profession = models.CharField(max_length=20)

   ## def prediction(self) {
      ##  print('call prediction functions here with data provided by this object ')
   ## }

    # identification personnelle

    # identification beneficiaire

    ##identification_beneficiaire = models.CharField(max_length=250, choices=type_identification)
