from django.db import models
from dos.script_one_client import predict


# Create your models here.

class Dos(models.Model):
    status_garantie = (
        ('False', 'False'),
        ('True', 'True')
    )

    type_client = (
        ('Physique', 'Physique'),
        ('moral', 'moral'),
        ('Autre', 'Autre')
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

    numero_compte = models.CharField(max_length=250)
    montant_pret = models.CharFieldField()
    taux_interet = models.CharField(max_length=10)
    viln = models.CharField(max_length=250)
    date_ouverture = models.DateField()
    date_naissance = models.DateField()
    statut_compte = models.CharField(max_length=250, choices=statut_compte)
    autre_garantie = models.CharField(max_length=10, choices=status_garantie)
    duree_remboursement = models.CharField(max_length=10)
    rythme_remboursement = models.CharField(max_length=20, choices=statut_remboursement)
    Profession = models.CharField(max_length=20)

    def prediction(self):
        print('call prediction functions here with data provided by this object')
        client_id = self.numero_compte
        new_client_data = {
            "client_id": self.numero_compte,
            "DNA": self.date_naissance,
            "year_DAN": self.date_naissance,
            "Typrt_Crédits Immobiliers ": self.motif_pret,
            "Typrt_Crédits Immobiliers": self.motif_pret,
            "RYTHREM_Mensuel": self.rythme_remboursement,
            "RYTHREM_Trimestriel": self.rythme_remboursement,
            "AUTGAR_False": self.autre_garantie,
            "AUTGAR_True": self.autre_garantie,
            "ID_INSTANCE_WORKFLOW": self.numero_compte,
            "Etat": "Etat",
            "ID'": self.numero_compte,
            "RYTHREM'": self.rythme_remboursement,
            "AUTGAR": self.autre_garantie,
            "Typrt": self.motif_pret,
            "Initiateur": "Initiateur",
            "Date_DerniereExecution": "Date_DerniereExecution",
            "DMO": "DMO",
            "DATDMDE": "DATDMDE",
            "ContentType": "ContentType",
            "Status": self.statut_compte,
            "EtatInterne": self.type_compte,
            "ibelleItem": "ibelleItem",
            "Montant": self.montant_pret,
            "Taux": self.taux_interet,

        }
        return predict(client_id, new_client_data)

# identification personnelle

# identification beneficiaire

##identification_beneficiaire = models.CharField(max_length=250, choices=type_identification)
