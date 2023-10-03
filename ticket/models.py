from django.db import models
from django.contrib.auth.models import User

# Create your models here. la base de données



class Ticket(models.Model):
    titre = models.CharField(max_lenght = 255)
    description =  models.CharField()
    date_creation = models.DateField()
    data_cloture = models.DateField(null=True)
    categorie = models.ManyToManyField(Categorie) #creer une table lien entre cat et ticket 
    createur = models.ForeignKey(User)
    CHOIX_ETAT = [
        ("C" , "créer"), 
        ("A" , "attente"), 
        ("E" , "en cours"), 
        ("T" , "terminer"),
    ]
    etat = models.CharField(choices=CHOIX_ETAT)
    


class Categorie(models.Model): 
    nom =  models.CharField(max_lenght = 255)



