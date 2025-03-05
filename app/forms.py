from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, NumberRange, Length

class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=120)])
    attending = RadioField('Will you attend?', 
                          choices=[('yes', 'Yes, I will attend'), ('no', 'Sorry, I cannot attend')],
                          default='yes')
    guests = IntegerField('Number of Additional Guests', validators=[Optional(), NumberRange(min=0, max=5)])
    dietary_restrictions = TextAreaField('Dietary Restrictions or Preferences', validators=[Optional(), Length(max=500)])
    message = TextAreaField('Message for the Host', validators=[Optional(), Length(max=1000)])
    submit = SubmitField('Submit Registration') 