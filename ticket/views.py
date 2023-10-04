from django.shortcuts import render
from .models import Message
from .form import MessageForm

# Create your views here.
def GetTicketMessages(request,id):
    messages = Message.objects.filter(ticket=id)
    return render(request,"ticket/messages.html",{"messages":messages})

def CreateTicket(request):
    if request.Method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message =  Message(
                
            )

def tmp(request):
    return render(request,"ticket/template/tmp.html")

def Acceuil (request):
	return render(request,'./Acceuil.html',{})
