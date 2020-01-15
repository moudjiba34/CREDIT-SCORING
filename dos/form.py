from django import forms
from dos.models import Dos


class DosForm(forms.Form):
    statut_operation_list = (
        ('Effectuee', 'EFFECTUEE'),
        ('En cours', 'EN COURS'),
    )

    reponse = (
        ('oui', 'oui'),
        ('non', 'non'),
    )



    type_client = (
        ('Physique', 'Physique'),
        ('moral', 'moral'),
        ('Autre', 'Autre')
    )

    statut_compte = (
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),

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
    status_garantie = (
        ('Oui', 'Oui'),
        ('Non', 'Non')
    )

    type_pret = forms.ChoiceField(choices=motif_pret, widget=forms.RadioSelect())
    numero_compte = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control m-input'}))
    type_client = forms.ChoiceField(choices=type_client, widget=forms.RadioSelect)
    montant_pret = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control m-input'}))
    taux_interet = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control m-input'}))
    viln = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control m-input'}))
    date_ouverture = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control m-input'}))
    date_naissance = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control m-input'}))
    statut_compte = forms.ChoiceField(choices=statut_compte, widget=forms.RadioSelect())
    autre_garantie = forms.ChoiceField(choices=status_garantie, widget=forms.RadioSelect())
    duree_remboursement = forms.CharField(max_length=20,
                                          widget=forms.TextInput(attrs={'class': 'form-control m-input'}))
    rythme_remboursement = forms.ChoiceField(choices=statut_remboursement, widget=forms.RadioSelect())
    Profession = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control m-input'}))
    type_identification = (
        ('Carte identité nationale', 'Carte identité nationale'),
        ('Passeport', 'Passeport'),
        ('Certificat de naissance', 'Certificat de naissance'),
        ('Permis de conduire', 'Permis de conduire'),
        ('Titre de séjour', 'Titre de séjour'),
        ('NINEA ET RC', 'NINEA ET RC'),
        ('Autre', 'Autre')
    )



    class Meta:
        # Provide an association between the ModelForm and a model
        model = Dos


class FormStepOne(forms.Form):
    statut_operation_list = (
        ('Effectuee', 'EFFECTUEE'),
        ('En cours', 'EN COURS'),
    )
    reponse = (
        ('oui', 'oui'),
        ('non', 'non'),
    )



class FormStepThree(forms.Form):
    piece_declaration = (
        ('Revenus sans raison économique correspondante', 'Revenus sans raison économique correspondante'),
        ('Le client refuse de fournir les informations demandées',
         'Le client refuse de fournir les informations demandées'),
        ('Présentation de faux documents', 'Présentation de faux documents'),
        ('Echange de petites coupures usagées contre des grosses coupures',
         'Echange de petites coupures usagées contre des grosses coupures'),
        ('Compte alimenté exclusivement par des transferts', 'Compte alimenté exclusivement par des transferts'),
        ('Le client est lésé et il refuse de porter plainte', ' Le client est lésé et il refuse de porter plainte'),
        ('Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées',
         'Préoccupation excessive du client sur la célérité avec laquelle les opérations seront exécutées'),
        ('Remboursement anticipé de prêts', 'Remboursement anticipé de prêts'),
        ('Transfert vers un paradis fiscal', 'Transfert vers un paradis fiscal'),
        ('Autre', 'Autre')
    )


class FormStepFour(forms.Form):
    type_client = (
        ('Physique', 'Physique'),
        ('moral', 'moral'),
        ('Autre', 'Autre')
    )

    statut_compte = (
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),

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
    status_garantie = (
        ('Oui', 'Oui'),
        ('Non', 'Non')
    )

    statut_compte = (
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),

    )
    status_garantie = (
        ('False', 'False'),
        ('True', 'True')
    )

    type_pret = forms.ChoiceField(choices=motif_pret)
    numero_compte = forms.CharField(max_length=250)
    type_client = forms.ChoiceField(choices=type_client)
    montant_pret = forms.FloatField()
    taux_interet = forms.CharField(max_length=10)
    viln = forms.CharField(max_length=250)
    date_ouverture = forms.DateField(widget=forms.SelectDateWidget())
    date_fermeture = forms.DateField(widget=forms.SelectDateWidget())
    statut_compte = forms.ChoiceField(choices=statut_compte)
    autre_garantie = forms.ChoiceField(choices=status_garantie)
    duree_remboursement = forms.IntegerField()
    rythme_remboursement = forms.ChoiceField(choices=statut_remboursement)
    Profession = forms.CharField(max_length=20)


class FormStepFive(forms.Form):
    type_identification = (
        ('Carte identité nationale', 'Carte identité nationale'),
        ('Passeport', 'Passeport'),
        ('Certificat de naissance', 'Certificat de naissance'),
        ('Permis de conduire', 'Permis de conduire'),
        ('Titre de séjour', 'Titre de séjour'),
        ('Pays de citoyenneté', 'Pays de citoyenneté'),
        ('Autre', 'Autre')
    )


