from django.shortcuts import render, redirect
from .models import Message, Ticket, Categorie
from django.http import JsonResponse
from datetime import datetime, date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



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

@login_required(redirect_field_name="login")
def CreaTicket(request):
    if request.method == "POST": 
            categorie = Categorie.objects.filter(pk__in=request.POST.get('categories','').split(","))
            print(request.POST.get('anonyme',False))
            ticket = Ticket(
                titre=request.POST.get('titre',''),
                description=request.POST.get('description',''),
                date_creation=date.today(),
                date_cloture=None,
                createur=request.user,
                etat="C",
                anonyme=(request.POST.get('anonyme',False)=="on"),
            )
            ticket.save()
            for cat in categorie:
                ticket.categorie.add(cat)
            ticket.save()
            return JsonResponse({})
    return redirect("/Acceuil/")
    
@login_required(redirect_field_name="login")
def Acceuil(request):
    categories = [[cat[0],cat[1]] for cat in Categorie.objects.all().values_list("pk","nom")]
    return render(request,'./Acceuil.html',{"categories":categories})

def GetTickets(request):
    qs = Ticket.objects
    Categorie = request.GET.get("categories",None)
    if Categorie:
        qs = qs.filter(categorie__in=Categorie.split(","))
    else:
        qs = qs.all()
    tickets = [ticket for ticket in qs.distinct().prefetch_related("createur").order_by("-date_creation").values_list("titre","description","date_creation","date_cloture","createur","etat","pk","anonyme")]
    return JsonResponse({"tickets":tickets})
    
def GetTicketDetail(resquest,id):
    ticket = Ticket.objects.filter(pk=id).prefetch_related("createur").values_list("titre","description","date_creation","date_cloture","createur__username","etat","anonyme").distinct()[0]
    return JsonResponse({"ticket":ticket})

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

@login_required(redirect_field_name="login")
def administration(request):
    # check if user is admin
    if not request.user.is_superuser:
        return redirect('/Acceuil/')
    users = [user.username for user in User.objects.all()]
    roles = [{"pk":role.pk,"nom":role.nom} for role in Categorie.objects.all()]
    return render(request, 'administration.html', {"users":users,"roles":roles})

@login_required(redirect_field_name="login")
def CreatUser(request):
    # check if user is admin
    if not request.user.is_superuser:
        return redirect('/Acceuil/')
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return JsonResponse({})
    return redirect("/Acceuil/")
        
def custom_logout(request):
    logout(request)
    
    return redirect('login')
