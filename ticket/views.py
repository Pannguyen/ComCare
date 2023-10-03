from django.shortcuts import render
from .form import CreationTicketForm
from .models import Ticket

# Create your views here.
def CreaTicket(request):
    if request.method == "POST": 
        form = CreationTicketForm(request.POST) #prendre le formulaire et remplir avec des données. 
        if form.is_valide(): #verifier si formulare est correct. 
            ticket = Ticket(
                titre = form.cleaned_data["titre"],
                description = form.cleaned_data["description pour ticket1"],
                date_creation = date.today(), 
                data_cloture = null(), 
                createur = request.User
            )
            ticket.save() #save dans la base de données.
    else :
        form = CreationTicketForm()     
    return HttpResponseRedirect("/", form)


            

