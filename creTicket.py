



# creTicket.py 

from flask import Blueprint, request, jsonify
from models import Ticket  # Importez votre modèle Ticket

create_ticket_bp = Blueprint('create_ticket', __name__)

@create_ticket_bp.route('/create_ticket', methods=['POST'])
def create_ticket():
    # Récupérez les données du formulaire
    data = request.json
    # Validez les données et effectuez les opérations nécessaires pour créer un nouveau ticket
    # Enregistrez le ticket dans la base de données
    new_ticket = Ticket(data['category'], data['description'])
    # Attribuez un identifiant unique au ticket
    new_ticket.save()
    # Retournez une réponse appropriée
    return jsonify({'message': 'Ticket créé avec succès'}), 201
