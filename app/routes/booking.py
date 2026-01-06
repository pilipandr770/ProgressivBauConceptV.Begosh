from flask import Blueprint, render_template, request, redirect, url_for, flash
import json
import os
from ..config import Config

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/termin-buchen', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        date = request.form.get('date')
        message = request.form.get('message')
        context = request.form.get('context', '')

        booking_data = {
            'name': name,
            'phone': phone,
            'email': email,
            'date': date,
            'message': message,
            'context': context
        }

        # Load existing bookings
        if os.path.exists(Config.BOOKINGS_FILE):
            with open(Config.BOOKINGS_FILE, 'r') as f:
                bookings = json.load(f)
        else:
            bookings = []

        bookings.append(booking_data)

        # Save
        with open(Config.BOOKINGS_FILE, 'w') as f:
            json.dump(bookings, f, indent=4)

        flash('Termin erfolgreich gebucht!')
        return redirect(url_for('main.index'))

    context = request.args.get('context', '')
    return render_template('booking.html', context=context)