from django.db import models
from django.contrib.auth.models import User

# Create your models here. la base de données

class Categorie(models.Model): 
    nom =  models.CharField(max_length = 255)

    def __str__(self):
        return self.nom

class Ticket(models.Model):
    titre = models.CharField(max_length = 255)
    description =  models.TextField()
    date_creation = models.DateField()
    date_cloture = models.DateField(null=True,blank=True)
    createur = models.ForeignKey(User,on_delete = models.CASCADE)
    # categorie = models.ManyToManyField(Categorie)
    CHOIX_ETAT = [
        ("C" , "créer"), 
        ("A" , "attente"), 
        ("E" , "en cours"), 
        ("T" , "terminer"),
    ]
    etat = models.CharField(max_length = 1,choices=CHOIX_ETAT)

    def __str__(self):
        return self.titre
    
