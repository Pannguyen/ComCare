from django.shortcuts import render
from .models import Message, Ticket
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
def GetTicketMessages(request,id):
    messages = [msg for msg in Message.objects.filter(ticket=id).prefetch_related("auteur").values_list("contenu","date_envoi","auteur__username")]
    return JsonResponse({"messages":messages})

def CreateTicket(request,id):
    if request.method == "POST":
        message =  Message(
            ticket = Ticket.objects.get(id=id),
            contenu = request.POST.get('msg', ''),
            date_envoi = datetime.now(),
            auteur = request.user,
        )
        message.save()
    return JsonResponse({})

def tmp(request):
    return render(request,"./tmp.html")

def Acceuil (request):
	return render(request,'./Acceuil.html',{})
