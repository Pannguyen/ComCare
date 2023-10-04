from django.shortcuts import render
from .form import CreationTicketForm
from .models import Ticket
from datetime import date 
from django.http import JsonResponse


#views.py
# Create your views here.


def CreaTicket(request):
    if request.method == "POST": 
            ticket = Ticket(
                titre=request.POST.get('titre',''),
                description=request.POST.get('description',''),
                date_creation=date.today(),
                date_cloture=None,
                createur=request.user
            )
            ticket.save()
            return JsonResponse({})
            
            
    
    return render(request, "./temporaire.html", {"form": CreationTicketForm()})

            

def Temporaire(request):
    return render(request,"./temporaire.html",{})


def login(request): 
    return render(request,"./login.html",{})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'temporaire.html', {'form': form})
    