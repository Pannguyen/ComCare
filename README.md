# ComCare

## **Introduction**

Le projet a pour but de corriger les problèmes liés à la communication au sein du campus. Pour ce faire, nous avons eu l'idée de développer une application web qui permettrait de faciliter la communication entre les étudiants et les professeurs.

Nous donnons la possibilité à toute personne de créer des tickets et nous les redirigeons automatiquement avec les personnes concernées par le ticket.


## **Fonctionalités**

- Création de ticket
- Filtrés les tickets
- discutée du probleme avec les personnes concernées
- ajouté de nouveau utilisateur (admin)
</br>
### future fonctionalité
- ajouté des fichiers au ticket
- messagerie instantanée
- affichée les tickets en fonction des personne consernées

***

## 🤖 **Technologies**
- language de programming  : [Python](https://www.python.org)
- FramWork : [Django](https://www.djangoproject.com)

***

## 💻 **Instalation**

#### **Prerequie** 

- [Python](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)

#### **Installation**

- Clonez le repository
- Installez les dependencies
```bash
pip install -r requirements.txt
```
- mettre a jour la base de donnée
```bash
py manage.py makemigrations
py manage.py migrate
```
- lancé le serveur
```bash
py manage.py runserver
```
- ouvrez votre navigateur et allez sur [localhost:8000/Acceuil/](http://localhost:8000/Acceuil/)
***
- pour ajouté un super utilisateur
```bash
py manage.py createsuperuser
```
- puis renseigné les informations demandé

***
## 👨‍💻 TEAM
>Sarrebourse Constantin

>CHEVALIER Maxime

>Nguyen Hoang Phuong Anh