from django.shortcuts import render, redirect
from .form import CreationTicketForm
from .models import Ticket
from datetime import date 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 



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


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'temporaire.html', {'form': form})


def login(request): 
    return render(request,"./login.html",{})

#vérifie simplement si le nom d'utilisateur et le mot de passe correspondent
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('nom_de_la_vue_de_succes')
        else:
            return render(request, 'login.html', {'error_message': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(request, 'login.html')



def navbar(request):
    return render(request, 'navbar.html')