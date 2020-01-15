from django.urls import path
from django.conf.urls import url
from . import views
from dos.views import *
from dos.form import *


app_name = 'dos'
urlpatterns = [
    url(r'^merci', views.index, name='index'),
    # path('', FormWizardView.as_view([FormStepOne, FormStepTwo])),
    #path('',FormWizardView.as_view([FormStepOne, FormStepTwo, FormStepThree, FormStepFour, FormStepFive, FormStepSix])),
    url('', views.ajout_dos, name='ajout_dos'),
    #path('', EnregistrementView.as_view()),
]
