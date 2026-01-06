from flask import Blueprint, render_template, send_from_directory
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(main_bp.root_path, '..', 'static'), 'robots.txt')

@main_bp.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(main_bp.root_path, '..', 'static'), 'sitemap.xml')
