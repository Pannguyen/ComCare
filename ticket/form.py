from django import forms  

class CreationTicketForm(forms.Form):
    titre = forms.CharField(label = "Titre du ticket", max_length = 255)
    description = forms.CharField(label = "desciption")
