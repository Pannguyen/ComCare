from django.shortcuts import render, redirect
from .models import Message, Ticket
from django.http import JsonResponse
from datetime import datetime, date
from django.contrib.auth import authenticate, login



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
                createur=request.user,
                etat="C",
            )
            ticket.save()
            return JsonResponse({})
    return redirect("/Acceuil/")
    

def Acceuil(request):
	return render(request,'./Acceuil.html',{})

def GetTickets(request):
    tickets = [ticket for ticket in Ticket.objects.all().prefetch_related("createur").order_by("-date_creation").values_list("titre","description","date_creation","date_cloture","createur","etat","pk")]
    return JsonResponse({"tickets":tickets})
    
def GetTicketDetail(resquest,id):
    ticket = Ticket.objects.filter(pk=id).prefetch_related("createur").values_list("titre","description","date_creation","date_cloture","createur__username","etat").distinct()[0]
    return JsonResponse({"ticket":ticket})

def navbar(request):
    return render(request, 'navbar.html')

def loginpage(request): 
    return render(request,"./login.html",{})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("redirect('/Acceuil/')")
            return redirect('/Acceuil/')
        else:
            return render(request, 'login.html', {'error_message': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(request, 'login.html')


def get_user_info(request):
    if request.user.is_authenticated:
        user_info = {
            "username": request.user.username,
        }
        return JsonResponse(user_info)
    else:
        return JsonResponse({})
        
def custom_logout(request):
    logout(request)
    return redirect('login')