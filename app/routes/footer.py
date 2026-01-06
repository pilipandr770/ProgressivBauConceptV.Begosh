from flask import Blueprint, render_template

footer_bp = Blueprint('footer', __name__)

@footer_bp.route('/impressum')
def impressum():
    return render_template('impressum.html')

@footer_bp.route('/agb')
def agb():
    return render_template('agb.html')

@footer_bp.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')