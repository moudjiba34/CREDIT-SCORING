from django.views.generic import TemplateView
from dos.form import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from dos.form import DosForm


# Create your views here.

def index(request):
    return HttpResponse("<h2> Formulaire Dos Enregistrer </h2>")


def ajout_dos(request):
    template_name = 'dos/dos_form.html'
    print("received post")
    if request.method == 'POST':
        print("confirmerd post")
        form = DosForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("hello form is submitted")
            # puisque c est un form simple  recupe
            # les champst et fait le save un p
            dossier = Dos()
            dossier.numero_compte = form.cleaned_data['numero_compte']
            dossier.montant_pret = form.cleaned_data['montant_pret']
            dossier.type_client = form.cleaned_data['type_client']
            dossier.taux_interet = form.cleaned_data['taux_interet']
            dossier.viln = form.cleaned_data['viln']
            dossier.duree_remboursement = form.cleaned_data['duree_remboursement']
            dossier.autre_garantie = form.cleaned_data['autre_garantie']
            dossier.rythme_remboursement= form.cleaned_data['rythme_remboursement']
            dossier.type_pret = form.cleaned_data['type_pret']
            dossier.date_ouverture = form.cleaned_data['date_ouverture']
            dossier.date_naissance = form.cleaned_data['date_naissance']
            dossier.statut_compte = form.cleaned_data['statut_compte']
            dossier.Profession = form.cleaned_data['Profession']
            dossier.save()
            resultat_prediction = dossier.prediction()
            print(resultat_prediction)
            redirect('dos:index')
        else:
            print("error form")
            print(form.errors)
    else:
        form = DosForm()
    return render(request, template_name, {'form': form})


class EnregistrementView(TemplateView):
    template_name = 'dos/dos_form.html'

    def get(self, request, *args, **kwargs):
        form = DosForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        if request.method == 'POST':
            form = DosForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                print("hello form is submitted")
            # form.save(commit=True)
            # form = DosForm()
            # return HttpResponse("<h2> Formulaire Dos Enregistrer </h2>")

            # return render(request, self.template_name, {'form': form})
