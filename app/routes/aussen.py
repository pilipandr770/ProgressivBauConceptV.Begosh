from flask import Blueprint, render_template
from ..services.service_loader import load_services

aussen_bp = Blueprint('aussen', __name__)

@aussen_bp.route('/aussenarbeiten')
def aussen():
    services = load_services('aussen')
    return render_template('aussen.html', services=services, agent_context='aussen')