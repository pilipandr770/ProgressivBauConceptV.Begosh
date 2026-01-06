from flask import Blueprint, request, jsonify
from .base_agent import BaseAgent
from .innen_agent import InnenAgent
from .aussen_agent import AussenAgent
from .elektro_agent import ElektroAgent
from .projekt_agent import ProjektAgent
from .welcome_agent import WelcomeAgent

chat_bp = Blueprint('chat', __name__)

agents = {
    'innen': InnenAgent,
    'aussen': AussenAgent,
    'elektro': ElektroAgent,
    'projekt': ProjektAgent,
    'welcome': WelcomeAgent
}

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    agent_key = data.get('agent', '')

    if agent_key not in agents:
        return jsonify({'response': 'Ungültiger Agent.'}), 400

    agent_class = agents[agent_key]
    agent = agent_class()
    response = agent.respond(message)

    return jsonify({'response': response})