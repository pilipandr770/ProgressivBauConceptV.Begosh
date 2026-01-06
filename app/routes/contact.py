from flask import Blueprint, render_template, request, redirect, url_for, flash
import json
import os
from ..config import Config

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/kontakt', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        context = request.form.get('context', '')

        contact_data = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
            'context': context
        }

        # Load existing contacts
        if os.path.exists(Config.CONTACTS_FILE):
            with open(Config.CONTACTS_FILE, 'r') as f:
                contacts = json.load(f)
        else:
            contacts = []

        contacts.append(contact_data)

        # Save
        with open(Config.CONTACTS_FILE, 'w') as f:
            json.dump(contacts, f, indent=4)

        flash('Nachricht gesendet!')
        return redirect(url_for('main.index'))

    context = request.args.get('context', '')
    return render_template('contact.html', context=context)