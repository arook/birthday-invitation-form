from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.forms import RegistrationForm
from app.models import Registration
from app.email_utils import send_confirmation_email
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # Convert form data to database model
        attending = True if form.attending.data == 'yes' else False
        
        # Check if email already exists
        existing_registration = Registration.query.filter_by(email=form.email.data).first()
        if existing_registration:
            flash('This email address has already been registered. Please use a different email.', 'error')
            return render_template('index.html', form=form)
        
        # Create registration record
        registration = Registration(
            full_name=form.full_name.data,
            email=form.email.data,
            phone=form.phone.data,
            age=form.age.data,
            attending=attending,
            guests=form.guests.data if attending else 0,
            dietary_restrictions=form.dietary_restrictions.data,
            message=form.message.data
        )
        
        # Save to database
        db.session.add(registration)
        db.session.commit()
        
        # Send confirmation email
        try:
            send_confirmation_email(registration)
            flash('Thank you for your registration! A confirmation email has been sent to your address.', 'success')
        except Exception as e:
            flash('Registration successful, but there was an error sending the confirmation email.', 'warning')
            print(f"Email error: {str(e)}")
        
        return redirect(url_for('main.thank_you'))
    
    # If form validation fails, flash errors
    if request.method == 'POST' and not form.validate():
        flash('There were errors in your form submission. Please check the fields and try again.', 'error')
    
    return render_template('index.html', form=form)

@main_bp.route('/thank-you')
def thank_you():
    return render_template('thank_you.html') 