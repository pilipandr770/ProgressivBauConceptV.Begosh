from flask import Blueprint, render_template
from ..services.service_loader import load_services

projekt_bp = Blueprint('projekt', __name__)

@projekt_bp.route('/projektleitung')
def projekt():
    services = load_services('projekt')
    return render_template('projekt.html', services=services, agent_context='projekt')