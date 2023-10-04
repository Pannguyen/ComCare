from django.shortcuts import render
from .models import Message, Ticket
from django.http import JsonResponse
from datetime import datetime, date


#views.py
# Create your views here.
def GetTicketMessages(request,id):
    messages = [msg for msg in Message.objects.filter(ticket=id).prefetch_related("auteur").values_list("contenu","date_envoi","auteur__username")]
    return JsonResponse({"messages":messages})

def CreateTicketMessage(request,id):
    if request.method == "POST":
        message =  Message(
            ticket = Ticket.objects.get(id=id),
            contenu = request.POST.get('msg', ''),
            date_envoi = datetime.now(),
            auteur = request.user,
        )
        message.save()
    return JsonResponse({})

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
    return render(request, "./temporaire.html", {})

            

def Temporaire(request):
    return render(request,"./temporaire.html",{})


def login(request): 
    return render(request,"./login.html",{})

# TOFIX : ah quoi sert cette fonction ?

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'temporaire.html', {'form': form})
    
from .models import Ticket
from django.http import JsonResponse
# Create your views here.
def Acceuil(request):
	tickets = [ticket for ticket in Ticket.objects.all().prefetch_related("createur").values_list("titre","description","date_creation","date_cloture","createur","etat","pk")]
	return render(request,'./Acceuil.html',{"tickets":tickets})
    
def GetTicketDetail(resquest,id):
    ticket = Ticket.objects.filter(pk=id).prefetch_related("createur").values_list("titre","description","date_creation","date_cloture","createur__username","etat").distinct()[0]
    return JsonResponse({"ticket":ticket})
    
