from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField



class ContactForm(FlaskForm):
    name = TextField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    subject = TextField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")