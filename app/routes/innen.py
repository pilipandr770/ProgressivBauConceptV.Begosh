from flask import Blueprint, render_template
from ..services.service_loader import load_services

innen_bp = Blueprint('innen', __name__)

@innen_bp.route('/innenausbau')
def innen():
    services = load_services('innen')
    return render_template('innen.html', services=services, agent_context='innen')