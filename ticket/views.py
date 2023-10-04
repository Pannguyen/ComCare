from django.shortcuts import render
from .models import Ticket
from django.http import JsonResponse
# Create your views here.
def Acceuil(request):
	tickets = [ticket for ticket in Ticket.objects.all().prefetch_related("createur").values_list("titre","description","date_creation","date_cloture","createur","etat","pk")]
	return render(request,'./Acceuil.html',{"tickets":tickets})
    
def GetTicketDetail(resquest,id):
    ticket = Ticket.objects.filter(pk=id).prefetch_related("createur").values_list("titre","description","date_creation","date_cloture","createur__username","etat").distinct()[0]
    return JsonResponse({"ticket":ticket})
    