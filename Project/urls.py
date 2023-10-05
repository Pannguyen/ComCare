"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from ticket.views import CreateTicketMessage, GetTicketMessages, Acceuil, CreaTicket, loginpage, GetTicketDetail, GetTickets, navbar, get_user_info, custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("CreateTicket/<int:id>/",CreateTicketMessage),
    path("GetTicketMessages/<int:id>/",GetTicketMessages),
    path('Acceuil/',Acceuil),
    path('creerTicket/', CreaTicket),
    path('login/', loginpage), 
    path('getticketdetail/<int:id>/',GetTicketDetail),
    path('gettickets/',GetTickets),
    path('loginme/', custom_login, name='login'),
    path('get_user_info/', get_user_info, name='get_user_info'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]

