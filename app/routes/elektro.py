from flask import Blueprint, render_template
from ..services.service_loader import load_services

elektro_bp = Blueprint('elektro', __name__)

@elektro_bp.route('/elektro')
def elektro():
    services = load_services('elektro')
    return render_template('elektro.html', services=services, agent_context='elektro')